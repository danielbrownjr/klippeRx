# SPDX-FileCopyrightText: 2026 Daniel Brown Jr.
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Synthetic schema tests, not printer observations."""
import json
import unittest

from klipperx_core.observation import UnknownReason, decode_observation
from klipperx_core.strict_json import EvidenceError


def fixture(**changes: object) -> bytes:
    record: dict[str, object] = {
        "schema": "1.0", "id": "obs-fixture-1",
        "printer_alias": "fixture-A", "source_id": "moon-status",
        "source_kind": "synthetic", "epoch": "boot-fixture",
        "seq": 7, "observed_utc": None, "received_utc": None,
        "monotonic_ms": 12000, "clock_quality": "unknown",
        "metric_id": "heater.actual_temperature", "unit": "degC",
        "value": None, "unknown_reason": "not_observed",
        "coverage": "partial",
    }
    record.update(changes)
    return json.dumps(record).encode("utf-8")


class ObservationTests(unittest.TestCase):
    def test_unknown(self) -> None:
        observation = decode_observation(fixture())
        self.assertIsNone(observation.value)
        self.assertEqual(observation.unknown_reason, UnknownReason.NOT_OBSERVED)

    def test_zero(self) -> None:
        observation = decode_observation(fixture(value=0, unknown_reason=None))
        self.assertEqual(observation.value, 0)
        self.assertIsNone(observation.unknown_reason)

    def test_rejections(self) -> None:
        cases = (
            ({"schema": "1.1"}, "schema"),
            ({"seq": True}, "counter"), ({"seq": -1}, "counter"),
            ({"monotonic_ms": 1.5}, "counter"),
            ({"unit": "F"}, "enum"), ({"source_kind": "target"}, "enum"),
            ({"id": "../secret"}, "token"), ({"metric_id": "unknown"}, "enum"),
            ({"extra": 1}, "fields"), ({"unknown_reason": None}, "unknown_reason"),
            ({"unknown_reason": "synthetic-secret"}, "unknown_reason"),
            ({"value": True, "unknown_reason": None}, "measurement"),
            ({"value": "0", "unknown_reason": None}, "measurement"),
            ({"value": 1}, "measurement"),
            ({"observed_utc": "2026-02-30T00:00:00Z"}, "timestamp"),
            ({"received_utc": "2026-01-01T00:00:00+01:00"}, "timestamp"),
            ({"received_utc": "2026-01-01T25:00:00Z"}, "timestamp"),
            ({"coverage": "all"}, "enum"), ({"clock_quality": "trusted"}, "enum"),
        )
        for changes, reason in cases:
            with self.subTest(changes=changes):
                with self.assertRaisesRegex(EvidenceError, "^" + reason + "$") as caught:
                    decode_observation(fixture(**changes))
                self.assertEqual(caught.exception.args, (reason,))
                self.assertIsNone(caught.exception.__cause__)
                self.assertIsNone(caught.exception.__context__)

    def test_all_unknown_reasons(self) -> None:
        for reason in UnknownReason:
            with self.subTest(reason=reason):
                observation = decode_observation(fixture(unknown_reason=reason.value))
                self.assertIsNone(observation.value)
                self.assertIs(observation.unknown_reason, reason)

    def test_missing_field(self) -> None:
        record = json.loads(fixture())
        del record["received_utc"]
        with self.assertRaisesRegex(EvidenceError, "^fields$"):
            decode_observation(json.dumps(record).encode())

    def test_signed_measurements_and_counter_bounds(self) -> None:
        for value in (-1.25, -9007199254740991, 9007199254740991):
            with self.subTest(value=value):
                observation = decode_observation(fixture(
                    value=value, unknown_reason=None, seq=0, monotonic_ms=9007199254740991
                ))
                self.assertEqual(observation.value, value)
                self.assertEqual(observation.seq, 0)
                self.assertEqual(observation.monotonic_ms, 9007199254740991)

    def test_accept_fixture_boundaries(self) -> None:
        payload = fixture(id="a" * 64, observed_utc="2024-02-29T00:00:00.123456Z",
                          received_utc="2024-02-29T00:00:01Z", clock_quality="utc",
                          coverage="complete", value=1.25, unknown_reason=None)
        observation = decode_observation(payload.ljust(2048, b" "))
        self.assertEqual(observation.id, "a" * 64)
        self.assertEqual(observation.observed_utc, "2024-02-29T00:00:00.123456Z")
        self.assertEqual(observation.received_utc, "2024-02-29T00:00:01Z")
        self.assertEqual(observation.clock_quality, "utc")
        self.assertEqual(observation.coverage, "complete")
        self.assertEqual(observation.value, 1.25)
        with self.assertRaisesRegex(EvidenceError, "^byte_limit$"):
            decode_observation(payload.ljust(2049, b" "))
        with self.assertRaisesRegex(EvidenceError, "^token$"):
            decode_observation(fixture(id="a" * 65))

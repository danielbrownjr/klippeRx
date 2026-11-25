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
            {"schema": "1.1"}, {"seq": True}, {"seq": -1},
            {"monotonic_ms": 1.5}, {"unit": "F"},
            {"source_kind": "target"}, {"id": "../secret"},
            {"metric_id": "unknown"}, {"extra": 1},
            {"unknown_reason": None}, {"unknown_reason": "other"},
            {"value": True, "unknown_reason": None},
            {"value": "0", "unknown_reason": None},
            {"value": 1}, {"observed_utc": "2026-02-30T00:00:00Z"},
            {"received_utc": "2026-01-01T00:00:00+01:00"},
            {"coverage": "all"}, {"clock_quality": "trusted"},
        )
        for changes in cases:
            with self.subTest(changes=changes):
                with self.assertRaises(EvidenceError):
                    decode_observation(fixture(**changes))

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

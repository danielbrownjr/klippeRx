# SPDX-FileCopyrightText: 2026 Daniel Brown Jr.
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Synthetic adversarial checks for the first local-core slice."""
import json
import unittest

from klipperx_core.strict_json import EvidenceError, decode_record


class StrictJsonTests(unittest.TestCase):
    def test_null_and_zero_are_distinct(self) -> None:
        self.assertEqual(decode_record(b'{"missing":null,"zero":0}'),
                         {"missing": None, "zero": 0})

    def test_invalid_records(self) -> None:
        cases = (
            (b'{"x":1,"x":2}', "duplicate_key"),
            (br'{"a":1,"\u0061":2}', "duplicate_key"),
            (b'{"x":-9007199254740992}', "integer_range"),
            (b'{"x":NaN}', "nonfinite"),
            (b'{"x":1e999}', "nonfinite"),
            (b'{"x":9007199254740992}', "integer_range"),
            (b'{"x":"\\ud800"}', "unicode"),
            (b'{"x":"\xff"}', "invalid_json"),
            (b'[]', "object_required"),
            (b'{"x":' + b'[' * 9 + b'0' + b']' * 9 + b'}', "depth_limit"),
            (b'{"x":[' + b','.join([b'0'] * 257) + b']}', "array_limit"),
            (b'{"x":"' + b'a' * 513 + b'"}', "string_limit"),
            (b' ' * 32769, "byte_limit"),
        )
        for payload, reason in cases:
            with self.subTest(reason=reason):
                with self.assertRaisesRegex(EvidenceError, "^" + reason + "$"):
                    decode_record(payload)

    def test_object_key_limit(self) -> None:
        boundary = {f"key{index}": 0 for index in range(64)}
        self.assertEqual(decode_record(json.dumps(boundary).encode("utf-8")), boundary)
        boundary["key64"] = 0
        with self.assertRaisesRegex(EvidenceError, "^key_limit$"):
            decode_record(json.dumps(boundary).encode("utf-8"))

    def test_record_specific_limit(self) -> None:
        with self.assertRaisesRegex(EvidenceError, "^byte_limit$"):
            decode_record(b'{"x":0}', limit=6)

    def test_accept_limits(self) -> None:
        record = {"x": [0] * 256, "s": "é" * 256, "n": -9007199254740991,
                  "p": 9007199254740991}
        payload = json.dumps(record, ensure_ascii=False).encode("utf-8")
        self.assertEqual(decode_record(payload.ljust(32768, b" ")), record)
        with self.assertRaisesRegex(EvidenceError, "^string_limit$"):
            decode_record(json.dumps({"s": "é" * 256 + "a"}).encode())

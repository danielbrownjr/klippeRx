# SPDX-FileCopyrightText: 2026 Daniel Brown Jr.
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Check structural depth independently of JSON string content."""
import json
import unittest
from unittest import mock

from klipperx_core import strict_json
from klipperx_core.strict_json import EvidenceError, check_bounds, decode_record


class DepthTests(unittest.TestCase):
    def test_string_delimiters_are_not_structure(self) -> None:
        for value in ('[' * 10, '"' + '[' * 10, '\\' + '{' * 10):
            with self.subTest(value=value):
                record = {"x": value}
                self.assertEqual(decode_record(json.dumps(record).encode()), record)

    def test_container_boundaries(self) -> None:
        for kind in ("array", "object"):
            for leaf in (0, "s", None):
                for depth in (8, 9):
                    with self.subTest(kind=kind, leaf=leaf, depth=depth):
                        value: object = leaf
                        for _ in range(depth - 1):
                            value = [value] if kind == "array" else {"x": value}
                        record = {"x": value}
                        payload = json.dumps(record).encode()
                        if depth == 8:
                            self.assertEqual(decode_record(payload), record)
                            check_bounds(record)
                        else:
                            with self.assertRaisesRegex(EvidenceError, "^depth_limit$"):
                                decode_record(payload)
                            with self.assertRaisesRegex(EvidenceError, "^depth_limit$"):
                                check_bounds(record)

    def test_backslash_before_structure(self) -> None:
        for depth in (8, 9):
            with self.subTest(depth=depth):
                value: object = 0
                for _ in range(depth - 1):
                    value = [value]
                record = {"x": "\\", "y": value}
                payload = json.dumps(record).encode()
                if depth == 8:
                    self.assertEqual(decode_record(payload), record)
                else:
                    with self.assertRaisesRegex(EvidenceError, "^depth_limit$"):
                        decode_record(payload)

    def test_deep_input_is_rejected(self) -> None:
        with self.assertRaisesRegex(EvidenceError, "^depth_limit$"):
            decode_record(b'{"x":' + b'[' * 1000 + b'0' + b']' * 1000 + b'}')

    def test_depth_rejected_without_decoding(self) -> None:
        payload = b'{"x":' + b'[' * 8 + b'0' + b']' * 8 + b'}'
        with (mock.patch.object(strict_json.json, "loads", side_effect=AssertionError("decoded")),
              self.assertRaisesRegex(EvidenceError, "^depth_limit$")):
            decode_record(payload)

    def test_truncated_deep_prefix_is_depth_limit(self) -> None:
        with self.assertRaisesRegex(EvidenceError, "^depth_limit$"):
            decode_record(b'{"x":' + b'[' * 8)

    def test_escape_state_resets_before_deep_structure(self) -> None:
        for escaped_string in ('"', "\\"):
            payload = (b'{"x":' + json.dumps(escaped_string).encode() + b',"y":'
                       + b'[' * 8 + b'0' + b']' * 8 + b'}')
            blocked_decoder = mock.patch.object(
                strict_json.json, "loads", side_effect=AssertionError("decoded")
            )
            with (self.subTest(escaped_string=escaped_string), blocked_decoder,
                  self.assertRaisesRegex(EvidenceError, "^depth_limit$")):
                decode_record(payload)

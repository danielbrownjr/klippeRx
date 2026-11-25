# SPDX-FileCopyrightText: 2026 Daniel Brown Jr.
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Bounded decoding for ordinary evidence records."""
import json
import math
from typing import Never

MAX_BYTES = 32 * 1024
MAX_INTEGER = 2**53 - 1
MAX_INTEGER_TOKEN_CHARS = 17
MAX_OBJECT_KEYS = 64
MAX_STRING_BYTES = 512
MAX_ARRAY_ITEMS = 256
MAX_DEPTH = 8
QUOTE = ord('"')
BACKSLASH = ord("\\")


class EvidenceError(ValueError):
    """Bounded classification; do not persist traceback frames or locals."""


def reject_constant(token: str) -> Never:
    raise EvidenceError("nonfinite")


def parse_integer(token: str) -> int:
    if len(token) > MAX_INTEGER_TOKEN_CHARS:
        raise EvidenceError("integer_range")
    value = int(token)
    if abs(value) > MAX_INTEGER:
        raise EvidenceError("integer_range")
    return value


def parse_float(token: str) -> float:
    value = float(token)
    if not math.isfinite(value):
        raise EvidenceError("nonfinite")
    return value


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    if len(pairs) > MAX_OBJECT_KEYS:
        raise EvidenceError("key_limit")
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise EvidenceError("duplicate_key")
        result[key] = value
    return result


def check_string(value: str) -> None:
    try:
        size = len(value.encode("utf-8"))
    except UnicodeError:
        pass
    else:
        if size > MAX_STRING_BYTES:
            raise EvidenceError("string_limit")
        return
    raise EvidenceError("unicode")


def check_bounds(value: object, depth: int = 1) -> None:
    if isinstance(value, (dict, list)) and depth > MAX_DEPTH:
        raise EvidenceError("depth_limit")
    if isinstance(value, str):
        check_string(value)
    elif isinstance(value, dict):
        for key, child in value.items():
            check_string(key)
            check_bounds(child, depth + 1)
    elif isinstance(value, list):
        if len(value) > MAX_ARRAY_ITEMS:
            raise EvidenceError("array_limit")
        for child in value:
            check_bounds(child, depth + 1)


def advance_depth(depth: int, byte: int) -> int:
    if byte in b"[{":
        depth += 1
        if depth > MAX_DEPTH:
            raise EvidenceError("depth_limit")
    elif byte in b"]}":
        depth -= 1
        if depth < 0:
            raise EvidenceError("invalid_json")
    return depth


def scan_depth(payload: bytes) -> None:
    depth = 0
    quoted = False
    escaped = False
    for byte in payload:
        if quoted:
            if escaped:
                escaped = False
            elif byte == BACKSLASH:
                escaped = True
            elif byte == QUOTE:
                quoted = False
        elif byte == QUOTE:
            quoted = True
        else:
            depth = advance_depth(depth, byte)


def decode_record(payload: bytes, *, limit: int = MAX_BYTES) -> dict[str, object]:
    if len(payload) > min(limit, MAX_BYTES):
        raise EvidenceError("byte_limit")
    scan_depth(payload)
    try:
        decoded: object = json.loads(
            payload.decode("utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
            parse_int=parse_integer,
            parse_float=parse_float,
        )
    except EvidenceError:
        raise
    except (ValueError, RecursionError):
        pass
    else:
        if not isinstance(decoded, dict):
            raise EvidenceError("object_required")
        check_bounds(decoded)
        return decoded
    # Raise outside the handler so the parser exception cannot retain raw input.
    raise EvidenceError("invalid_json")

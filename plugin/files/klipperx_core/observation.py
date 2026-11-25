# SPDX-FileCopyrightText: 2026 Daniel Brown Jr.
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Synthetic-only observation schema 1.0."""
import re
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

from .strict_json import EvidenceError, decode_record


class UnknownReason(StrEnum):
    NOT_OBSERVED = "not_observed"
    UNSUPPORTED = "unsupported"
    STALE = "stale"
    INCOMPLETE = "incomplete"
    INVALID = "invalid"
    REDACTED = "redacted"
    CLOCK_UNCERTAIN = "clock_uncertain"


@dataclass(frozen=True, slots=True)
class Observation:
    schema: str
    id: str
    printer_alias: str
    source_id: str
    source_kind: str
    epoch: str
    seq: int
    observed_utc: str | None
    received_utc: str | None
    monotonic_ms: int
    clock_quality: str
    metric_id: str
    unit: str
    value: int | float | None
    unknown_reason: UnknownReason | None
    coverage: str


FIELDS = frozenset(Observation.__dataclass_fields__)
TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
UTC = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,6})?Z")


def token(value: object) -> str:
    if not isinstance(value, str) or TOKEN.fullmatch(value) is None:
        raise EvidenceError("token")
    return value


def counter(value: object) -> int:
    if type(value) is not int or value < 0:
        raise EvidenceError("counter")
    return value


def timestamp(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or UTC.fullmatch(value) is None:
        raise EvidenceError("timestamp")
    try:
        datetime.fromisoformat(value)
    except ValueError:
        pass
    else:
        return value
    raise EvidenceError("timestamp")


def choice(value: object, allowed: tuple[str, ...]) -> str:
    if not isinstance(value, str) or value not in allowed:
        raise EvidenceError("enum")
    return value


def measurement(value: object, reason: object) -> tuple[int | float | None, UnknownReason | None]:
    if value is None:
        if not isinstance(reason, str):
            raise EvidenceError("unknown_reason")
        try:
            return None, UnknownReason(reason)
        except ValueError:
            pass
        raise EvidenceError("unknown_reason")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or reason is not None:
        raise EvidenceError("measurement")
    return value, None


def decode_observation(payload: bytes) -> Observation:
    """Validate a fixture record; this does not authenticate its provenance."""
    record = decode_record(payload, limit=2048)
    if record.keys() != FIELDS:
        raise EvidenceError("fields")
    if record["schema"] != "1.0":
        raise EvidenceError("schema")
    source = choice(record["source_kind"], ("synthetic",))
    metric = choice(record["metric_id"], ("heater.actual_temperature",))
    unit = choice(record["unit"], ("degC",))
    value, reason = measurement(record["value"], record["unknown_reason"])
    return Observation(
        schema="1.0",
        id=token(record["id"]),
        printer_alias=token(record["printer_alias"]),
        source_id=token(record["source_id"]),
        source_kind=source,
        epoch=token(record["epoch"]),
        seq=counter(record["seq"]),
        observed_utc=timestamp(record["observed_utc"]),
        received_utc=timestamp(record["received_utc"]),
        monotonic_ms=counter(record["monotonic_ms"]),
        clock_quality=choice(record["clock_quality"], ("unknown", "utc")),
        metric_id=metric,
        unit=unit,
        value=value,
        unknown_reason=reason,
        coverage=choice(record["coverage"], ("partial", "complete")),
    )

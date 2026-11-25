# Local evidence core

Initial M1.1-A draft slice. Pure Python 3.11 standard library, no runtime dependencies or printer access.

Run synthetic tests from the repository root:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=plugin/files python3.11 -m unittest discover -s plugin/tests -v

The decoder rejects duplicate keys, malformed UTF-8, nonfinite numbers, unsafe integer ranges, excessive depth, keys, arrays and strings. It checks the ordinary record byte cap before decoding. Error classifications exclude raw payload text. This is not a transport decoder or a complete evidence schema validator.

A frozen observation model validates the documented synthetic example, exact fields, schema 1.0, opaque tokens, nonnegative counters, UTC timestamp syntax, null/reason pairing and one fixture metric/unit pair. Source kind is synthetic only; clock quality and coverage labels are provisional fixture choices. Structural depth counts only nested JSON objects and arrays, with the root object at level 1. The maximum is eight container levels, regardless of scalar leaves. The same limit is enforced before and after decoding. Production catalog, cross-record ordering, freshness, scoped coverage, field-specific limits for other record types, and remaining evidence models are pending. No manifest, service, storage, UI or deployment is provided. No acceptance gate closes with this slice.

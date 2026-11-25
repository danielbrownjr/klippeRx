# Changelog

## Unreleased

- Add the first bounded strict JSON decoder and synthetic adversarial tests.
- Add a frozen synthetic observation schema 1.0 model with exact fields, typed counters, UTC timestamps, fixture metric/unit and null/reason validation.
- Reject excessive structural nesting before JSON decoding and cover the 65-key rejection boundary with a synthetic regression test.
- Align pre-decode and post-decode nesting limits at eight container levels, including the root object. Add exact boundary, escape and decoder-order regression tests, numeric typing refinement and synthetic fixture boundary coverage.
- Name evidence bounds and separate structural depth accounting without changing the record contract; test escaped strings followed by excessive depth before decoding.
- Establish a local-core source and test layout, without an installable manifest.
- Detach internal decoder and validation exceptions from bounded rejection classifications. Test exact classifications, exception context isolation and additional synthetic observation acceptance paths.

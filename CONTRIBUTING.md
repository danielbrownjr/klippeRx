# Contributing

Start with the issue, [development contract](CLAUDE.md) and [approved decisions](docs/decisions/0001-engineering-foundation.md). Implementation needs scoped owner authorization. Local fixture work does not authorize installation or access to real devices.

## Layout

The intended single-plugin layout follows Bespok3D: `plugin/manifest.json`, `plugin/files/`, `plugin/doc/README.md`, `plugin/doc/CHANGELOG.md`, `plugin/doc/ATTRIBUTIONS.md`, `plugin/tests/run.sh`, `plugin/requirements.txt` when needed; root `scripts/check.sh`, `scripts/tag_version_guard.sh`, `lib_bespok3d/` and `.github/workflows/` when commissioned. The builder sees the plugin directory, not arbitrary conventional Python source roots. No empty placeholder implementation, manifest, tests or workflows are shipped by this foundation change. Actual service package placement must be reviewed against the supported builder.

## Verification and review

Use the pinned shared baseline and [verification ownership](docs/verification.md). No unreviewed dependency installation. Agents may run only authorized inspected non-Git checks in isolation. The owner executes unchanged Git-dependent checks and full required gate. Required skips are blockers. Record exact candidate inventory and artifact hashes, tool versions, test scope and failures. Independent reviews remain source-read-only and report-only. A design review is not product approval.

Maintain docs and regression tests with changes. Use meaningful commits and DCO signoff; the owner controls Git and release actions. Every version bump includes the matching user-facing changelog entry. Never claim hardware support based on host tests, or publish without explicit owner approval.

## Reporting issues

Include a minimal synthetic reproducer, exact supported versions where relevant, observed evidence and expected versus actual behavior. Remove private identifiers, credentials and log contents before posting. For security concerns use [SECURITY.md](SECURITY.md).

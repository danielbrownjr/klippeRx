# KlippeRx development contract

KlippeRx is a planned embedded Bespok3D diagnostic plugin. Initial scope is passive observation, deterministic diagnostics, bounded evidence and advisory output. Normal printer operation is independent of the plugin.

## Plugins declare WHAT, never HOW

Declare supported resources and permissions. The daemon and adapter own install, routing, service lifecycle and recovery. No plugin-managed installer, private watchdog, system interpreter replacement or printer recovery script. Do not invent platform capabilities.

## House rules

- Rule Zero: no em dashes or en dashes in authored material, including comments, commits, PRs and docs. Preserve unmodified third-party license text.
- Domain-meaningful identifiers; no single-letter or role-free names. Flatten nesting using guard clauses, named functions and lookups; justify necessary nesting.
- One responsibility per file/function. Aim for 80-100 lines per file; about 150 is the ceiling. Split by concern. Extract the third duplication, not speculative abstractions.
- Extend upstream minimally and additively if separately authorized. Never rewrite vendor methods or patch vendor UI as an integration shortcut.
- Never commit real credentials, IPs, hostnames, UUIDs, serials or private diagnostic data. Use synthetic fixtures and documentation addresses.
- Write less first; prefer stdlib and existing reviewed helpers. Classes only where state warrants. Typed Python signatures, no leaking Any, exactly one final newline.

## Change workflow

Read actual manifest, files tree and plugin/doc/README.md when present, relevant issue and approved design. Work to a scoped user story. Verify source evidence rather than assume. Fixes require regression tests proven to fail on old behavior in a disposable workspace. Update behavior docs and changelog with changes. Run applicable shared checks through the split ownership in docs/verification.md. Fix causes; only a justified per-instance gate allowance where permitted, never blanket suppression. Missing required checks remain blocked. Distinguish documented, inspected, inferred, proposed, host-tested and physically measured results.

## Authority and safety

- Never run Git, even read-only, or indirectly via gate/build scripts, hooks or alternative tooling. Owner alone manages Git history, commits, branches, tags and pushes. Do not use APIs to circumvent this. No tracker mutations without explicit authority.
- Never delete repository files outright; move to ignored _trash/ with reason and report. Preserve originals before substantial replacement; disclose build-generated replacement behavior and use isolated builds.
- No live printer access without applicable authorization, no mutation without explicit per-action approval. Never open unknown serial/GPIO links. No heater, motion, print, restart, firmware or configuration command interface in M1.
- No package installation into system, Klipper or Moonraker Python. Offline private venv through daemon only.
- No upstream contact, signing, release, publication or credential use without separate approval. No private reference files or session identifiers in public artifacts; no attribution trailers.
- Human commands one per code block. Owner signs off commits using DCO; version bump commits start with version. Each printer test build needs a distinct patch version and matching changelog entry; docs alone do not warrant a bump. No product version assigned by this documentation bootstrap.
- Never substitute host results for printer performance. Independent reviews are source-read-only/report-only with only explicitly approved isolated verification; one initial review and at most one focused re-review unless new material blockers justify more.

See docs/architecture.md, docs/security-model.md, docs/resource-budgets.md, docs/evidence-contract.md and docs/verification.md. If intent is materially unclear, ask one specific question and stop.

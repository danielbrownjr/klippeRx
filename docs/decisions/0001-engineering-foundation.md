# ADR 0001 - Engineering foundation

Status: accepted design, 2026-11-25. Implementation and acceptance are separate.

Adopt one embedded passive diagnostic service, account-free local diagnostics, optional user-triggered external inference, trusted browser including mobile, native protected provisioning, trusted administrators/installed plugins, bounded persistent credential rollback protection and daemon-owned lifecycle. No hostile-root or full-image anti-rollback claim. PC-A through PC-D required and unresolved; PC-E conditional. Adopt CPython 3.11, aiohttp, strict JSON, bounded SQLite, prebuilt static assets and AGPL-3.0-or-later for original work. Pin shared main 5e3396caf698f165ad15228c49561a32280a20a0. Approve resource ceilings in resource-budgets.md and split verification ownership. One exact U1 target pending identification. No prior-art copying approved.

| Gate | Status | Required acceptance |
| --- | --- | --- |
| C1 | OPEN | Supported protected provisioning and trusted access |
| C2 | OPEN | Protected custody and bounded lifecycle/restore behavior |
| C3 | OPEN | Actual isolation/access evidence under selected trust model |
| C4 | OPEN | Physical resource/print impact measurements |
| C5 | OPEN | Supported provider, billing, consent and integration |
| C6 | OPEN | Exact installed profile and artifact correspondence |
| C7 | OPEN | Nontechnical mobile/browser usability |
| C8 | OPEN | Target TLS/CA/clock/DNS acceptance |
| C9 | OPEN | Dependency, license, package, gate and release acceptance |
| C10 | Future blocked | Daemon-managed live transactions; outside M1 |

F01-F10 design deliverables accepted. Issue closure records design acceptance only. No product tests, target access, implementation or release readiness follow from this decision. Next proposed work: independently authored local-core fixtures after separate authorization.

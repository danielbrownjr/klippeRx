# Security policy

KlippeRx is in design-stage development. No supported production release exists. C1-C9 remain open; do not install experimental artifacts on a working printer without explicit owner-controlled acceptance.

The approved initial trust boundary assumes trusted administrators and trusted installed plugins. It does not protect against hostile root processes, privileged sibling services or undetectable whole-device rollback. Private browser access requires trusted transport and scoped authorization. Secrets require protected platform custody and lifecycle invalidation, not ordinary persistent plugin files. No printer control or live configuration writes in M1.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting for this repository if enabled. If unavailable, open a minimal issue asking the maintainer for a private reporting channel; do not disclose exploit details, credentials, private logs or printer/network identifiers publicly. No response-time guarantee is established. Do not test against devices or accounts without authorization.

See [security model](docs/security-model.md) for the proposed enforcement requirements and unresolved dependencies.

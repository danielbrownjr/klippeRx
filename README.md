# KlippeRx

**Diagnose. Understand. Print.**

KlippeRx is a planned intelligent printer diagnostic application for Klipper-based 3D printers, designed for installation through the Bespok3D ecosystem.

## Project objectives

- Lightweight, passive monitoring and evidence-based local diagnostics without an AI account.
- Trusted browser access, including mobile, through supported platform facilities.
- Optional AI-assisted troubleshooting through supported provider APIs, with explicit metering and per-request consent.
- Safe, read-only configuration inspection; offline configuration organization is a later milestone.

## Safety by design

The initial application is observation-only. No arbitrary G-code, heater or motor control, live configuration writes, service restarts, autonomous maintenance or model-driven tools. Printer operation must not depend on KlippeRx or external inference.

## Initial target and status

The engineering foundation has owner approval. The first target is one exact Snapmaker U1 hardware/firmware/platform profile, still to be identified and verified. There is no production package, verified hardware compatibility, or supported credential/browser integration yet. All C1-C9 acceptance gates remain open. The next milestone is M1.1, initially limited to separately authorized local-core fixture development.

## Development roadmap

- [x] M0: Technical feasibility
- [x] M0-S: Consumer experience feasibility
- [x] M1.0-R: Engineering foundation (design acceptance only)
- [ ] M1.1: Embedded local diagnostics
- [ ] M1.2: Security and credential lifecycle
- [ ] M1.3: AI provider integration
- [ ] M1.4: Physical U1 acceptance
- [ ] M1.5: Consumer release readiness

## Engineering documentation

- [Architecture](docs/architecture.md)
- [Security model](docs/security-model.md)
- [Resource budgets](docs/resource-budgets.md)
- [Runtime and dependency direction](docs/runtime.md)
- [Consumer experience](docs/consumer-experience.md)
- [Evidence contract](docs/evidence-contract.md)
- [Verification](docs/verification.md)
- [Approved decisions](docs/decisions/0001-engineering-foundation.md)
- [Contribution guide](CONTRIBUTING.md)

## License and ecosystem

Original KlippeRx work is licensed under AGPL-3.0-or-later; see [LICENSE](LICENSE). Third-party components retain their respective licenses.

- [Bespok3D](https://github.com/Bespok3d)
- [Klipper](https://www.klipper3d.org/)
- [Moonraker](https://moonraker.readthedocs.io/)

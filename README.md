# KlippeRx

**Diagnose. Understand. Print.**

KlippeRx is an intelligent printer diagnostic application for Klipper-based 3D printers, designed for installation through the Bespok3D ecosystem.

## Project Objectives

- Simple installation through Bespok3D.
- Accessible, browser-based printer diagnostics.
- Persistent, lightweight printer monitoring.
- Useful local diagnostics without an AI account.
- Optional AI-assisted troubleshooting through supported provider APIs.
- Safe, read-only configuration inspection.
- Evidence-based maintenance recommendations.
- Future offline configuration organization and validation.

## Safety by Design

KlippeRx is initially an observation-only application. It does not execute arbitrary G-code, control heaters or motors, modify active printer configuration, restart services, or perform autonomous maintenance.

AI-generated recommendations are advisory. Printer safety and normal operation must remain independent of the application and external AI providers.

## Initial Hardware Target

Snapmaker U1 through Bespok3D, subject to hardware compatibility, security, and resource acceptance testing.

## Development Roadmap

- [x] M0: Technical feasibility
- [x] M0-S: Consumer experience feasibility
- [ ] M1.0-R: Engineering foundation
- [ ] M1.1: Embedded local diagnostics
- [ ] M1.2: Security and credential lifecycle
- [ ] M1.3: AI provider integration
- [ ] M1.4: Physical U1 acceptance
- [ ] M1.5: Consumer release readiness

## Development Status

Early engineering and architecture development. No production release or verified hardware compatibility is currently claimed.

## Ecosystem

- [Bespok3D](https://github.com/Bespok3d)
- [Klipper](https://www.klipper3d.org/)
- [Moonraker](https://moonraker.readthedocs.io/)

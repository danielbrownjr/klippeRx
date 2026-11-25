# Runtime and dependency direction

## F05 - Approved runtime, dependency and license direction

Use CPython 3.11, one asyncio process, one passive collector and one bounded SQLite worker thread/connection. aiohttp handles HTTP/WS; strict stdlib JSON validation, dataclasses and enums; prebuilt static HTML/CSS/JS without CDN, external fonts or target Node. No separate provider SDK, MCP SDK, ASGI stack, template interpreter, numerical framework or model runtime. Pure versioned authored rules, bounded reviewed regex only. No arbitrary code, macros or rule loading. Candidate stack approved, exact shipped dependency set still requires artifact/security/target acceptance. Private daemon-managed venv is dependency separation, not a privilege boundary.

Builder targets manylinux2014_aarch64, CPython 3.11, ABI cp311/abi3/none, binary wheels only. Use private root requirements mode, not shared Klipper interpreter requirements. Published daemon v0.14.0 creates venv via target python3 -m venv and performs offline pip install --no-index --no-deps of explicit wheels; launch via supported $PLUGIN_VENV/bin/python3. No runtime online resolution or plugin-managed interpreter replacement. Verify actual target ABI/libc and native imports. No fabricated manifest permissions.

| Distribution | Candidate version | SPDX license |
| --- | --- | --- |
| aiohttp | 3.14.5 | Apache-2.0 AND MIT |
| aiohappyeyeballs | 2.7.1 | PSF-2.0 |
| aiosignal | 1.4.0 | Apache-2.0 |
| attrs | 26.1.0 | MIT |
| frozenlist | 1.8.0 | Apache-2.0 |
| multidict | 7.2.1 | Apache-2.0 |
| propcache | 0.5.4 | Apache-2.0 |
| typing-extensions | 4.16.0 | PSF-2.0 |
| yarl | 1.25.1 | Apache-2.0 |
| idna | 3.20 | BSD-3-Clause |

The candidate wheel filename/hash/metadata register must be supplied and reviewed before dependency acquisition; this table is not a lockfile. Reported compressed bytes 3,225,976; expanded member bytes 12,968,898. Five native and five pure Python wheels. No installation, import, full resolver execution, advisory clearance or target ABI verification yet. Include typing-extensions on 3.11; no async-timeout or extras. Reevaluate changes rather than silently substitute. Acquire exact version-specific official wheels with hashes, independently validate marker closure, tags, inventory and metadata. Reject unexpected files, sdists, VCS requirements, unreviewed installer hooks. Builder presence check is not closure validation. Exact toolchain and inputs recorded; two clean unsigned builds, compare payload and full archive separately. No reproducibility claim from payload equivalence alone.

SQLite candidate: one connection owned by one worker; journal_mode=DELETE, synchronous=FULL, bounded transactions and batched aggregates; no initial WAL. Verify target _sqlite3, compile options and filesystem semantics. Limit entire owned state, not just max_page_count; reserve journal/temp space before writes, avoid full VACUUM during printing. Database failure leaves bounded memory-only observations and pauses persistence/export. Credentials and authority ledger outside evidence DB. Separate Moonraker/provider client sessions; fixed allowlists; disable credential-bearing redirects, ambient proxy inheritance and cross-boundary cookie reuse. Verified hostname/TLS, bounded decoded/wire sizes and deadlines. No insecure CA fallback. PC-A-D remain unresolved.

AGPL-3.0-or-later approved for original KlippeRx work; the root LICENSE supplies the unmodified license text. Preserve third-party notices, including aiohttp's bundled llhttp MIT notice, platform component relationships, and applicable source delivery obligations. Independent authorship; no prior-art code copying before separate reuse review. No assumption that separate processes automatically remove license obligations. CycloneDX JSON SBOM per unsigned candidate, separate build tool inventory; exact package URLs/versions/hashes/runtime graph, platform-provided CPython/OpenSSL/SQLite and frontend assets. Match actual artifact, not desired requirements. Preserve vendor license texts unmodified. Advisory review pending. Host tools separate, exact closure subject to review/provisioning; Tool versions and closure require approval before installation. C6/C9 OPEN.

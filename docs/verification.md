# Verification and acceptance

## F07 - Approved shared gate and evidence ownership

Pin shared library main 5e3396caf698f165ad15228c49561a32280a20a0 (archive SHA-256 39acdeda59620178976f5121bba8fa8a1a0629884178cf17b97d70cc34ed5ab0, 89794 bytes, 57 entries, historical archive and reported current correspondence). Do not replace with dev 8ea114b3a3405b4761478549e4e26124707b26e7. Core helpers equivalent in reviewed revisions; main Ruff stricter. Neither old main CI nor dev workflow is a reproducible pinned tooling environment by itself. Node 24 host direction, exact patch/digest and all tool closures pending. No install authorization. Before execution, review the complete check matrix, prerequisites, side effects and exact selected call chains. No shared gate modifications or waivers. R = exact future candidate root; T = pinned tooling directory; E = approved preprovisioned tool env; O = isolated output directory. Commands below are design records only.

| Check | Ownership / applicable invocation |
| --- | --- |
| Rule Zero | Agent eligible: node "$T/em-dash-guard.mjs" <authored paths> --suffix .html --suffix .yml --suffix .yaml --suffix .cfg --suffix .conf --suffix .tmpl; explicit additional excluded authored assets; vendor text excluded with rationale |
| Workflow / release policy | Agent eligible: node "$T/workflow-pinning-detector.mjs" "$R"; node "$T/release-trigger-detector.mjs" "$R"; absent actual workflow N/A, not CI clearance |
| Manifest origin | the owner only: node "$T/manifest-origin-detector.mjs" "$R" through unchanged manifest_origin_check; real origin; no-origin pass insufficient |
| Manifest validity | Agent inspection against exact supported daemon/adapter/builder; no complete standalone schema CLI established; unknown fields not proof |
| Detector self-tests | Agent eligible after reviewed glob: node --test "$T"/*.test.mjs (four inspected main modules; disposable TMPDIR) |
| Full shared self gate | the owner only: bash scripts/check.sh at pinned library root; Git and tool bootstrap side effects |
| Ruff | Agent eligible: "$E/bin/ruff" check --config "$T/ruff.toml" <actual Python paths> |
| mypy | Agent eligible: "$E/bin/mypy" --config-file "$T/mypy.ini" <actual Python paths>; reviewed imports/plugins |
| Pytest | Agent eligible: "$E/bin/pytest" -c "$T/pytest.ini" --rootdir . --tb=short -q <reviewed fixture paths>; no broad upstream discovery |
| Shell | Agent eligible: shellcheck <authored shell files>; bash -n or sh -n as appropriate; extensionless included |
| REUSE | the owner only: unchanged stock reuse_per_file_check, Git enumeration |
| Tool bootstrap | Not agent authorized; b3d_python_tools/b3d_build_tool_venv may remove venv, fetch/install floating tools |
| Workflow validation | Agent eligible: actionlint <actual workflows>, all-action full SHA review, approved tool; the owner owns actual CI |
| Build and wheel bake | Owner-controlled pending exact call-chain review and separate build permission; reviewed builder commands and hashes; no Git-dependent paths by agents |
| Package/SBOM/advisories | Agent inspection eligible after authorization, exact tools and artifact; safe paths, wheel closure, notices, hashes, actual inventory; advisory network separately reviewed |
| CI and release | Agent read-only inspection; the owner owns exact candidate provenance, Git, CI triggers, signing/publication; no clean CI claim with blocking runtime warnings |
| Target / independent review | the owner-controlled separately authorized target campaign; source-read-only report-only reviewer under GSO |

All agent eligibility conditional on separately authorized execution, reviewed transitive calls, isolated side effects and pinned tools. Run lint/type/test from R with outputs in O. No Git commands or substitutes, fabricated origins, gate edits, auto-install or mutation to obtain a pass. Stock gate may skip required checks yet report success. Use per-check PASS/FAIL/BLOCKED/justified N/A ledger, exact candidate SHA plus complete source/inventory hashes including relevant dirty/untracked inputs, tool/config/fixture hashes, invocation, environment, exit/counts, logs, side effects and coverage. the owner runs unchanged required Git-dependent/full gate checks against same candidate; no required skips waived. Compare manifests before/after; changed source/deps/manifest/rules/schema/fixtures invalidate affected evidence. Independent review and physical acceptance separate. C6/C9 OPEN. No product gate executed.

## F10 - Verification strategy

### Test environment and evidence classes

Separate pure deterministic unit tests, isolated fake-peer integration, package/target build, supported platform integration, physical acceptance and release review. Every case records ID, candidate SHA or immutable artifact hash, fixture version/hash, platform/profile, prerequisites, command, expected versus actual, duration, outcome PASS/FAIL/BLOCKED/NOT_APPLICABLE, logs sanitized and limitations. No test executed in this design task. Agent checks require inspected no-Git transitive commands and isolated writable outputs; Approved F07 and investigation section 9 define exact commands and ownership. the owner executes Git-dependent checks, evidence tied to same candidate. Do not replace Git invocations or claim full gate pass from subsets. No host dependency installation or external network by fixtures. Default-deny egress and no real printer/provider addresses; explicit test injection, no production fallback. Review test imports/plugins/conftest, bound queue and payloads. Fake Moonraker HTTP/WS peer binds only isolated test transport, records every requested operation, rejects all nonallowlisted operations, supports partial deltas, disconnect/reconnect, wrong identity, huge/malformed payload, stale/duplicate/out-of-order sequence and clock changes. Fake provider uses explicit injected isolated transport, never production TLS bypass, and records envelope/digest and request count, synthetic key only, deterministic timeout before/after receipt, 401/429/5xx, oversize, redirect and malicious text; no real endpoints or credentials. Fake authority models PC-A-D as explicit assumptions, not platform proof. Inject monotonic and wall clocks, bounded storage and crash points. Never deliberately fill actual printer storage or stop core services. Use disposable synthetic files and controlled fault injection.

| ID | Gate | Case and objective pass condition |
| --- | --- | --- |
| V01 | C1 | Wrong owner/install/provider/epoch, expired or concurrent grant, ambiguous commit: no unauthorized commit; at most one successful operation, safe status query |
| V02 | C1/C3 | Substituted initial certificate, wrong Host/Origin, DNS rebinding, same-host port cookie, sibling host injection, direct backend, forged header, encoded route, stream/download: no private bytes or effects; actual browser trust required later |
| V03 | C1/C2 | Logout/revoke during stream, polling through idle expiry, wall clock jump, restart: terminate access within approved revocation bound; no background extension |
| V04 | C2/C3 | Synthetic secret through permission normalization, repair, backup, exports, logs, crash output: zero canary leakage and no widened permissions under supported platform contract |
| V05 | C2 | Disconnect/replace/update/uninstall/reinstall/known restore/transfer with interruption at each state: no revived authorization in bounded scope; local versus remote revocation reported separately |
| V06 | C2 | Restore whole image including authority and keys: negative model documents undetectable replay outside guarantee; no false universal anti-rollback claim |
| V07 | C3 | Inspect exact target UID/GID/groups, files, socket and origin boundary; wrong local principal rejected where contract requires; hostile root explicitly outside scope |
| V08 | C4 | One collector, quota/journal/temp and reserve faults, reconnect storm, CPU/RSS/traffic bounds: fixture caps hold, target measurements separately meet approved F06 windows |
| V09 | C4 | Baseline/candidate representative existing print observation after separate approval: no new MCU timing warning, disconnect or material print-impact anomaly; stop on anomaly or reserve breach |
| V10 | C5 | Provider disconnected/expired, changed consent bytes/model/account, duplicate click, revoke race, timeout after possible send, rate limit: no unauthorized send, no silent retry/fallback, uncertainty visible; real provider test separate |
| V11 | C6 | Exact supported board, firmware/fork, B3 versions, ABI, package and source hashes match approved register; mismatch blocks support claim |
| V12 | C7 | Install/launch/pair/skip/diagnose/export/disconnect/return user tasks, mobile/keyboard/reader/offline: no manual infrastructure, no accidental dispatch, critical tasks complete |
| V13 | C8 | Invalid/expired TLS chain, wrong hostname, clock/DNS errors, redirect, timeout/oversize: fail closed; no credential forwarding; target CA/clock/DNS verified separately |
| V14 | C9 | Pinned dependencies, notices/SBOM, package closure, manifest/workflow/source checks and exact candidate review: applicable full gate evidence including owner Git checks; no publication without approval |
| V15 | F09/C4 | Duplicate keys, nonfinite, unknown schema, null versus zero, wrong units, oversize/depth, stale epoch, partial delta: bounded rejection or explicit unknown, no invented fact |
| V16 | F09/C1 | Malicious logs/macros, path traversal/symlink, arbitrary URL/SQL, prompt injection, provider HTML: no control capability, no escape, no executable rendering or unauthorized disclosure |
| V17 | F09/C5 | Export digest changes, omitted/uncertain secret, modified provider parameters, oversized required evidence: preview invalidated or export denied, exact approved evidence only |
| V18 | F01/C4 | Collector crash, offline provider, store failure, unavailable authority: no printer effect, local core continues where possible, private access fails closed, stale gaps explicit |

### Coverage and closure

C1 V01-V03,V16-V17 plus approved PC-A/C protocol and exact client acceptance; C2 V03-V06 plus protected PC-B/D storage/lifecycle; C3 V02,V04,V07 plus approved residual boundary and actual target evidence; C4 V08-V09,V15,V18 plus F06 budgets; C5 V10,V17 plus current provider terms and separately authorized real inference; C6 V11; C7 V12; C8 V13; C9 V14. Each remains OPEN until corresponding decision and actual evidence. Mock successes cannot close platform/physical gates. C10 not in scope. Physical permissions: read-only target profile acquisition separately authorized; install, update, reboot, uninstall/reinstall and recovery each separately authorized with known-good route; observation of representative existing print separately approved, no agent-started print, heaters/motion/service manipulation. Stop immediately on new MCU timing warning, disconnect, abnormal scheduling, memory/storage reserve breach, unauthorized request or identity mismatch; preserve bounded evidence and ask owner to decide recovery, no private watchdog. Approved F06 stop criteria and measurement accounting above apply.

### Review and sequencing

F05-F07 investigation returned and stack/license/budgets/baseline/target scope/split ownership approved. Reconciled limits and accounting above control all affected V cases. Exact target identity, tool closure, provider contracts, schema implementation and physical acceptance remain pending. Design approval is not implementation authorization. F01-F04 review is prior design review, not code approval. For bounded implementation, one independent initial source-read-only review and at most one focused independent re-review after substantive remediation, following GSO. Extra review only for material new/unresolved blockers or changed safety/security architecture; archive complete sanitized findings separately. No claim CI clean without exact-head applicable evidence and absence of blocking warnings. Local-core fixture work can proceed only on separate authorization and cannot establish consumer release readiness. F08-F10 reconciled design baseline adopted under owner direction. Tighter schema caps, aggregate channel sizing assumption and formative UX sample remain design choices subject to implementation verification. Design issue closure does not close acceptance gates.

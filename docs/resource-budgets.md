# Resource and retention budgets

## F06 - Approved target scope and resource acceptance

Exactly one board/firmware/platform combination; identity pending. Source-described constrained nominal 512 MB class is MemTotal <=640*1024 KiB; standard above threshold, described 1 GB+; neither is actual measured unit memory. Historical handoff reports aarch64, Buildroot/BusyBox/glibc, CPython 3.11.8 and SOABI cpython-311-aarch64-linux-gnu. Exact installed facts unknown. Require actual board, SoC/core count, memory, kernel/OS, libc/loader, python3 and private venv version/ABI, _sqlite3/version/options, OpenSSL/CA/DNS/clock, Klipper/Moonraker fork versions/objects, B3 installed daemon/adapter/desktop hashes, process UID/GID/filesystem/socket policy, writable mounts/blocks/inodes, sibling workloads and browser/OS profiles. Do not infer compatibility from release source or historical data. Unknown/untested profiles excluded; no second class qualification by analogy. The complete installed-profile register must be established before target acceptance.

| Metric | Approved ceiling / accounting |
| --- | --- |
| Steady CPU | mean <=2% of one core over 10 min, all owned process user+system time |
| Printing CPU | p95 <=5% at 1 Hz, >=600 samples, nearest rank ceil(.95*N), gaps explicit |
| Diagnosis CPU | mean <=10% of one core over 60 s, all extraction/cleanup |
| RSS | <=48 MiB steady maximum 1 Hz sum in warmed 10 min; <=64 MiB peak across sampled modes; PSS separately where available |
| Package / installed | <=30 / 80 MiB, entire package and installed venv/wheels/assets/bytecode; apparent and allocated bytes; upgrade copies separate |
| State | <=64 MiB including journals/temp/logs; 16 DB + 17 journal reserve + 8 incidents + 8 logs + 8 exports/temp + 7 metadata/slack MiB |
| Logs | <=8 MiB included in state, normal <1 MiB/day; repeated faults rate limited |
| Free space | available >=max(128 MiB,10% writable filesystem), including worst-case writes, stricter adapter policy wins |
| Telemetry | one selective subscription; retained thermal <=1 Hz; fallback >=5 s active / >=30 s idle plus bounded backoff/jitter |
| Observation traffic | <10 KiB/s mean over 10 min both directions; UI/cloud and total separate |
| Detailed ring | <=10 min AND <=4 MiB in memory, included in RSS |
| Aggregate / incidents | <=72 h minute buckets / <=7 days, quotas first |
| Service / UI | healthy <=10 s from launch; useful cold-cache LAN/mobile view <=2 s |
| API / clients | p95 <=250 ms for bounded reads; <=4 simultaneous UI sessions, no per-client collector |
| Work queue | <=64 bounded jobs; no unbounded accumulation |
| Provider | one inflight, no hidden queue, <=1/min and 30/day configurable lower; connect <=5 s, idle <=15 s, total <=60 s |

Measure plugin process tree plus separately attributable gateway/broker overhead and whole-host pressure. Retention is not guaranteed duration. Keep byte caps, quotas and free-space reserves independently enforced. For design sizing only, propose at most 16 aggregate channels initially: 4,320 buckets/channel over 72 h = 69,120 rows; at an assumed 96 bytes/row including index contribution ~6.33 MiB, before SQLite page/free-list/metadata overhead. This is a planning assumption, not measured SQLite size or a requirement to retain 16 channels. Validate actual row/index/page sizes and reduce channels or duration before quota breach. Detailed ring similarly bounded by bytes, independent of incoming WS cadence. Unknown/unchanged values do not imply connection failure. Liveness, expected source cadence, source time and observation age tracked separately.

Future measurement protocol: freeze complete candidate/target/workload; record memory, available space/inodes, process identity and instrumentation overhead. Owner selects comparable ordinary print conditions, siblings unchanged. Warm baseline and candidate >=10 min idle and >=10 min representative printing each, 1 Hz CPU/RSS/network; PSS ~30 s if available. CPU percent =100*delta(user+system ticks)/(CLK_TCK*elapsed monotonic seconds); PID plus start time, account exited children/gaps. Include four sessions, bounded extraction and 60 s diagnosis with approved fake provider. Measure startup, >=20 cold-cache samples and separate warm samples, median/p95/outliers. Check allocated/apparent bytes, f_bavail*f_frsize, journal/recovery copies and log growth; mark unmeasured daily rate explicitly. Stop on new unexplained timing warning, disconnect/shutdown, abnormal scheduling, OOM/swap distress, reserve breach, sustained ceiling failure or unexpected interaction; owner controls recovery, plugin stops its own optional work only. No intentional printer disk filling, power cuts or core service kills. Every target access and maintenance action separately authorized. C4/C6 OPEN; no measured fit.

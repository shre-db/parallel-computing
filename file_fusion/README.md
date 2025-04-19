# 🔐 File Fusion

**Field**: Data Archiving / Forensics\
**Objective**:
Use multithreading to quickly scan thousands of log files (from multiple sources), then merge them into a single chronological timeline based on timestamps.

Core Concepts
---
- Threaded I/O: reading files in parallel to speed things up.
- Parsing structured logs: extracting timestamps.
- Efficient merging of sorted data from multiple sources.
- Thread-safe aggregation of results.

Use Case Scenario
---
You're the lead engineer at a security firm. You need to merge logs from thousands of sensors after a suspected cyber breach. Each log is time-stamped. You have 2 minutes to reconstruct the timeline.

Step-by-Step Plan
---
1. Simulate 1,000+ log files.
2. Each log file contains 50–100 lines with random timestamps.
3. Use ThreadPoolExecutor to read files in parallel.
4. Parse and collect all lines into a shared list.
5. Sort the entire collection by timestamp.
6. Save to a merged file: `merged_timeline.log`.

Sample Log Line Format
---
```log
2023-04-19 14:53:01.123 [INFO] User logged in
2023-04-19 14:53:02.456 [ERROR] Connection failed
```

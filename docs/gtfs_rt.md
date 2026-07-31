## GTFS-RT Raw Snapshot Storage (written in 31.July.2026)
- Approximately 432 GB of raw GTFS-RT (1week) .pb files are currently stored in S3, costing about $7.6 so far.
- Raw files should be retained for future validation and reprocessing, but continued growth will increase storage costs.

### Resolution 
Use S3 as the authoritative store for raw data; keep only a small subset locally for development.

- [] Evaluate lossless compression—preferably Zstandard (.zst)—using one hour of snapshots to measure compression ratio and processing time.

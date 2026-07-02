#!/bin/bash

export PATH="$HOME/.local/bin:$PATH"

cd "$(dirname "$0")/.." || exit 1

mkdir -p logs

uv run python src/gtfs/ingest_gtfs_rt.py >> logs/ingest_gtfs_rt.log 2>&1
#!/usr/bin/env bash

set -euo pipefail

# Project root = parent directory of scripts/
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# dirname "$0" returns the directory containing the current script. 
# We then move one level up (..) and use pwd to obtain the absolute path. 
# This ensures the script works correctly regardless of the current working directory.


mkdir -p \
    "$PROJECT_ROOT/src"/{ingestion,processing,gis,rl,gnn,visualization,utils} \
    "$PROJECT_ROOT/tests" \
    "$PROJECT_ROOT/data"/{raw,processed,exports} \
    "$PROJECT_ROOT/notebooks" \
    "$PROJECT_ROOT/docker" \
    "$PROJECT_ROOT/infrastructure"/{aws,github_actions} \
    "$PROJECT_ROOT/archive" \
    "$PROJECT_ROOT/docs"

touch \
    "$PROJECT_ROOT/README.md" \
    "$PROJECT_ROOT/src/__init__.py" \
    "$PROJECT_ROOT/docs/architecture.md" \
    "$PROJECT_ROOT/docs/design_decisions.md" \
    "$PROJECT_ROOT/docker/Dockerfile" \
    "$PROJECT_ROOT/docker/docker-compose.yml"

echo "Project structure created under:"
echo "$PROJECT_ROOT"
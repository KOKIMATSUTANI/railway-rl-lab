# Open Railway Intelligence
An Open-Source AI Framework for Railway Traffic Management

## Table of Contents

- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Repository Structure](#repository-structure)
- [Current Status](#current-status)  
Last Update on 14.Jul.2026
- [Documentation](#documentation)
- [Future Direction](#Future-Direction)

# Project Overview
- Collect railway infrastructure data (e.g., tracks, switches, signals, and platforms) from OpenStreetMap (OSM).
- Integrate timetable and real-time operational data from GTFS and GTFS-Realtime.
- Construct a dynamic railway graph by combining static infrastructure and real-time operational information.
- Develop intelligent railway traffic management using machine learning, with a primary focus on reinforcement learning.
- Build an open, extensible, and reproducible framework for railway traffic optimization.
# Motivation

Railway delays remain one of the biggest challenges in modern railway operations, particularly in Germany.

This project aims to investigate how modern AI techniques can support railway traffic management by combining:

- 🗺️ **OpenStreetMap (OSM)** for railway infrastructure.
- 🚆 **GTFS-Realtime** for dynamic operational information.
- 🧠 **Graph Neural Networks (GNNs)** for railway network representation.
- 🤖 **Reinforcement Learning (RL)** for traffic optimization.
- ☁️ **AWS Cloud Services** for scalable and practical deployment.
- ⚛️ **Quantum Computing** as a future direction for solving complex railway optimization problems.

## Why Open Source?

Many railway optimization studies rely on proprietary operational data that cannot be reproduced.

This project instead focuses on:

- Building a fully reproducible research framework.
- Using only publicly available datasets.
- Bridging academic research and real-world railway operations.
- Developing technologies that could eventually be deployed in practical railway systems.



# Repository Structure
```text

├── README.md
├── data
│   ├── processed
│   ├── raw
│   └── test
├── docker
│   ├── Dockerfile
│   ├── Dockerfile.gtfs_rt_ingest
│   └── docker-compose.yml 
├── docs
│   ├── graph.md
│   ├── gtfs_rt.md
│   ├── osm.md
│   └── rl.md
├── infrastructure
│   ├── aws
│   └── github_actions
├── logs
│   └── ingest_gtfs_rt.log
├── pyproject.toml
├── scripts
│   ├── init_project.sh
│   └── run_gtfs_rt_ingestion.sh
├── src
│   ├── __init__.py
│   ├── archive
│   ├── gnn
│   ├── graph
│   ├── gtfs
│   ├── gtfs_rt
│   ├── osm
│   ├── rl
│   ├── train.py
│   ├── utils
│   └── visualization
└── uv.lock
```

## infrastructure



# Documentation

# Current Status

## 1. Infrastructure Modeling
- [x] Railway infrastructure (OSM)
- [x] Station metadata
- [ ] Signal & switch modeling

## 2. Operational Data
- [x] GTFS Static
- [x] GTFS Realtime

## 3. Graph Construction
- [x] Data preprocessing
- [ ] Graph generation
- [ ] Feature engineering

## 4. AI Models
- [ ] GNN
- [ ] RL
- [ ] GNN + RL integration

## 5. Deployment
- [x] Docker (for GTFS realtime ingestion with )
- [ ] AWS
- [ ] Continuous data collection

# References

# License

# Future Direction 
The ultimate goal is to build an open-source platform for intelligent railway traffic management that can contribute to reducing delays in real-world railway operations while remaining extensible to future technologies.

## ideas
- NeTEx 
- Deutsche Bahn API (German Railway API)

- Multi Agent Deep Reinforcement Learning (MADRL)
- Quantum Computing / Quantum Machine Leaning (QML)
- Mix Integer Linier Programming (MILP) 
- Long Short-Term Memory (LSTM)
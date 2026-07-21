# Open Railway Intelligence
An Open-Source AI Framework for Railway Traffic Management

## Table of Contents

- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Repository Structure](#repository-structure)
- [Current Status](#current-status)  
Last Update on 18.Jul.2026
- [Future Direction](#future-direction)
- [Reference](#references)
- [Data Sources](#data-sources)

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


# Repository Structure
```text

├── README.md
├── data
│   ├── raw
│   └── processed
├── docker
│   └──  Dockerfile.gtfs_rt_ingest
├── docs
│   ├── osm.md
│   ├── gtfs_rt.md
│   ├── graph.md
│   └── rl.md
├── src
│   ├── __init__.py
│   ├── osm
│   ├── gtfs_rt
│   ├── graph
│   ├── gnn
│   ├── rl
│   ├── train.py
│   └── visualization
├── pyproject.toml
└── uv.lock
```

# Current Status
## 1. Infrastructure Modeling
- [x] Overpass query development for the Dresden railway network
- [x] GeoJSON-based railway data validation
- [x] Automated OpenStreetMap data acquisition via Overpass API
- [x] Railway infrastructure preprocessing
- [x] Station metadata extraction
- [x] Signal and switch extraction

## 2. Operational Data

### 2.1 GTFS Static
- [x] GTFS Static ingestion

### 2.2 GTFS Realtime
- [x] GTFS Realtime ingestion  
- [x] Docker containerization 
- [x] AWS Fargate deployment
- [x] Automated GTFS-Realtime data collection with AWS (Fargate&EventBridge) 
- [ ] Data preprocessing for generating Graph 


## 3. Graph Construction
- [x] Prototype graph generation (dummy data)
- [ ] Graph generation with real railway data (PyTorch Geometric)

## 4. AI Models
- [x] Prototype reinforcement learning environment
- [ ] GNN implementation
- [ ] RL environment with real railway network
- [ ] Reward function design
- [ ] GNN + RL integration
- [ ] Training & evaluation

## Future Direction 
The ultimate goal is to build an open-source platform for intelligent railway traffic management that can contribute to reducing delays in real-world railway operations while remaining extensible to future technologies.

## ideas
- 
- NeTEx 
- Deutsche Bahn API (German Railway API)

- Multi Agent Deep Reinforcement Learning (MADRL)
- Quantum Computing / Quantum Machine Leaning (QML)
- Mix Integer Linier Programming (MILP) 
- Long Short-Term Memory (LSTM)

# References
## References

- Fouladi, A., Okhrin, O., & Bešinović, N. (2026). *Real-time microscopic train rescheduling using graph neural network based reinforcement learning*. SSRN Preprint. https://doi.org/10.2139/ssrn.6604465

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.


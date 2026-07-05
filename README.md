# Dresden Rail Analytics Lab

A research-oriented project for analyzing railway infrastructure and timetable data in the Dresden (VVO) region.

This project explores how geospatial railway data from OpenStreetMap / OpenRailwayMap and timetable data from GTFS can be combined into a unified graph-based representation for downstream analysis, visualization, and machine learning tasks.

The current focus is on:

- Extracting and validating railway infrastructure data using Overpass API
- Processing GTFS timetable data for temporal modeling
- Building graph representations of railway networks
- Experimenting with reinforcement learning (RL) and graph neural networks (GNNs)
- Developing visualization tools for spatial and temporal analysis




# Railway-RL-Lab

A research-oriented project combining **Reinforcement Learning (RL)**, **Graph Neural Networks (GNNs)**, and **geospatial railway infrastructure data**.

This project explores how railway infrastructure data (OpenStreetMap / OpenRailwayMap + GTFS) can be transformed into graph-based representations and used for simulation, analysis, and reinforcement learning environments.

---

## 🚆 Project Goals

* Extract railway infrastructure data from **OpenStreetMap / OpenRailwayMap (Overpass API)**
* Integrate **GTFS timetable data**
* Build a **graph representation of railway networks**
* Apply:

  * Reinforcement Learning (RL)
  * Graph Neural Networks (GNNs)
* Visualize railway systems and learned behaviors
* Optionally deploy with **Docker + AWS CI/CD pipelines**

---

## 🧠 System Overview

```
data/raw → ingestion → processing → graph (GN / GIS) → RL / GNN → visualization
```

Key idea:

> Convert real-world railway infrastructure into a learnable graph environment.

---

## 📁 Project Structure

```
src/
├── gtfs/             # Data acquisition (GTFS-rt)
├── overpass/         # Raw Overpass API experiments
├── processing/       # Parsing, graph building, feature engineering
├── gis/              # GeoJSON / PostGIS integration
├── rl/               # Reinforcement learning environment & training
├── gnn/              # Graph neural network models
├── visualization/    # Maps, dashboards, TensorBoard logging
├── utils/            # Utilities & helpers
```

```
data/
├── raw/              # Raw API outputs (Overpass, GTFS)
├── processed/        # Cleaned datasets
└── exports/          # Final outputs (GeoJSON, Parquet, etc.)
```

---

## Data
### 1. OpenRailwaymap 
### 2. GTFS
### 3. GTFS-rt

## Future Work

### priority 2
- Optimize Docker image size by separating research and runtime dependencies.
- Reduce container startup time for cloud deployment.
- Improve dependency management for production environments. 

## ⚙️ Setup

### 1. Install dependencies

Using `uv` (recommended):

```bash
uv sync
```

or manually:

```bash
pip install -r requirements.txt
```

---

### 2. Activate environment (optional)

```bash
source .venv/bin/activate
```

or simply:

```bash
uv run python
```

---

## 📊 Data Exploration
### jq installation
``` bash
sudo apt update
sudo apt install jq
```

### Quick inspection with `jq`

```bash
jq '.elements | length' data/raw/dresden_railway.json
jq -r '.elements[].tags.railway // empty' data/raw/dresden_railway.json | sort | uniq -c
```

---

### JupyterLab

```bash
uv add --dev jupyterlab
uv run jupyter lab
```

---

## 🗺 Example Notebook

Explore Dresden railway infrastructure:

```
notebooks/dresden_explorer.ipynb
```

---

## 🧪 Overpass Experiments

Example scripts:

* `src/overpass/railway_dresden.py`
* `src/overpass/railway_test_tokyo.py`

These scripts query railway infrastructure data from OpenStreetMap using Overpass API.

---

## 🐳 Docker (optional)

```bash
docker-compose up --build
```

Used for environment reproducibility and future ML scaling.

---

## ☁️ Future Extensions

* PostGIS integration for spatial queries
* AWS-based CI/CD pipeline
* Distributed training for RL/GNN models
* Real-time visualization dashboard

---

## 📌 Notes

* `data/raw/` is not versioned (large geospatial datasets)
* `.venv/` is managed by `uv`
* Experiments in `overpass/` are used for validation and exploration before productionizing into `src/`

---

## 🚀 Vision

This project aims to bridge:

* Railway infrastructure systems
* Graph-based machine learning
* Reinforcement learning environments
* Real-world geospatial data pipelines

into a unified experimental research framework.

---

もし次やるなら、このREADMEはかなり強い土台になってるので、次は

* architecture図（MermaidでOK）
* RL環境の定義（Gymっぽい設計）
* Graph構造定義（node/edge設計）

あたり書くと一気に“研究プロジェクト感”出る。

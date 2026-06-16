# Dresden Rail Analytics Dashboard

An interactive web application built with Streamlit that integrates rail infrastructure data from OpenRailwayMap (OpenStreetMap) and schedule data from GTFS (General Transit Feed Specification) for the Dresden area (VVO network).

This tool visualizes railway capabilities (such as maximum speed limits and electrification status) alongside dynamic timetable schedules, providing an integrated spatial-temporal overview for transit analysis and rescheduling research.

## Features

- **Infrastructure Mapping**: Visualizes tracks, switches, and line properties (e.g., `maxspeed`, `electrified`) using OpenRailwayMap/OSM attributes.
- **Timetable Integration**: Parses static GTFS feeds to display real-time/scheduled arrivals, departures, and routing for major hubs like Dresden Hauptbahnhof.
- **Spatial Filtering**: Dynamic filtering of infrastructure features based on maximum speed thresholds and line operational types.
- **High-Performance Rendering**: Utilizes a dual-frontend approach using Folium for standard interactive components and Pydeck (WebGL) for dense geometric visualizations.

## Project Structure

```text
dresden-rail-app/
│
├── data/
│   ├── raw/                  # Excluded from Git. Holds raw .osm/.pbf and GTFS .zip files.
│   └── processed/            # Contains preprocessed GeoJSON and Parquet files for fast loading.
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py      # Script to extract and preprocess OSM/GTFS data into lightweight formats.
│   └── helpers.py            # Core analytical logic (spatial queries, timetable filtering).
│
├── app.py                    # Main Streamlit application entry point.
├── requirements.txt          # Project dependencies.
└── README.md                 # Project documentation.
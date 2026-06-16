import requests
import json
from pathlib import Path

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

DATA_DIR = Path("~/prep/opendata_rl_railway/data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

query = """
[out:json][timeout:60];

(
  way["railway"](35.67,139.75,35.69,139.78);

  node["railway"="signal"](35.67,139.75,35.69,139.78);

  node["railway"="switch"](35.67,139.75,35.69,139.78);

  node["railway"="station"](35.67,139.75,35.69,139.78);

  way["railway"="platform"](35.67,139.75,35.69,139.78);
);

out body;
>;
out skel qt;
"""

headers = {
    "User-Agent": "KokiRailwayProject/1.0"
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36(Research Project: datadriven-dispatch; contact: info@example.com)"
    
}

response = requests.post(
    OVERPASS_URL,
    data=query,
    headers=headers,
    timeout=120
)

response.raise_for_status()

data = response.json()



with open(DATA_DIR / "tokyo_station_railway.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"{len(data['elements'])} objects saved.")
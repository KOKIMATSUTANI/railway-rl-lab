from pathlib import Path
import time
from datetime import datetime

import requests
from google.transit import gtfs_realtime_pb2

from zoneinfo import ZoneInfo

# ==========================
# Settings
# ==========================
URL = "https://realtime.gtfs.de/realtime-free.pb"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAVE_DIR = PROJECT_ROOT / "data" / "raw" / "gtfs_rt"


SAVE_DIR.mkdir(parents=True, exist_ok=True)

# This script is started by crontab and stops at the end time defined below.
BERLIN = ZoneInfo("Europe/Berlin")

END_TIME = datetime(
    2026, 7, 2, 7, 18, 0,
    tzinfo=BERLIN
)

INTERVAL = 15  # seconds

# ==========================
# Download loop
# ==========================


while datetime.now(BERLIN) < END_TIME:
    try:
        # Download GTFS-RT
        print(f"Request start : {datetime.now(BERLIN)}")

        response = requests.get(URL, timeout=30)
        response.raise_for_status()
        print(f"Response end  : {datetime.now(BERLIN)}")

        # Download timestamp 
        download_dt = datetime.now(BERLIN)

        # Parse protobuf
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)

        # Feed generation timestamp (Unix -> datetime)
        header_ts = feed.header.timestamp
        feed_dt = datetime.fromtimestamp(header_ts, BERLIN)

        # Create filename
        filename = (
            SAVE_DIR
            / f"{feed_dt:%Y%m%d_%H%M%S}_dl{download_dt:%H%M%S}.pb"
        )

        # Save file
        filename.write_bytes(response.content)

        print(
            f"Saved: {filename.name} "
            f"(Feed={feed_dt:%Y-%m-%d %H:%M:%S}, "
            f"Download={download_dt:%Y-%m-%d %H:%M:%S})"
        )

    except Exception as e:
        print(f"Error: {e}")

    # Wait INTERVAL seconds
    time.sleep(INTERVAL)
from pathlib import Path
import time
from datetime import datetime, timedelta

import requests
from google.transit import gtfs_realtime_pb2

from zoneinfo import ZoneInfo


import os 
import boto3

import json


# ==========================
# Settings
# ==========================
# GTFS-RT URL (default: GTFS.de)
GTFS_URL = os.getenv("GTFS_URL", "https://realtime.gtfs.de/realtime-free.pb")

# Env variables for Storage 
# if you'd like to store at S3, use own bucket name 
STORAGE = os.getenv("STORAGE", "local")
BUCKET_NAME = os.getenv("BUCKET_NAME", "your-bucket-name")


# Create local save directory
if STORAGE == "local":
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    SAVE_DIR = PROJECT_ROOT / "data" / "raw" / "gtfs_rt"
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
# Create S3 client if storage is set to S3
elif STORAGE == "s3":
    s3 = boto3.client("s3")
 
# Timezone and run duration
GTFS_TIMEZONE = ZoneInfo(os.getenv("GTFS_TIMEZONE","Europe/Berlin"))
RUN_MINUTES = int(os.getenv("RUN_MINUTES", "3"))

# Start and end time for the download loop
START_TIME = datetime.now(GTFS_TIMEZONE)
END_TIME = START_TIME + timedelta(minutes=RUN_MINUTES)

# Interval between downloads (in seconds)
INTERVAL = int(os.getenv("INTERVAL", "30"))  # seconds


config = {
    "GTFS_URL": GTFS_URL,
    "STORAGE": STORAGE,
    "RUN_MINUTES": RUN_MINUTES,
    "INTERVAL": INTERVAL, 
    "BUCKET_NAME": BUCKET_NAME if STORAGE == "s3" else None,
}

print(json.dumps(config, indent=2))

# ==========================
# Download loop
# ==========================





while datetime.now(GTFS_TIMEZONE) < END_TIME:
    
    loop_start = time.monotonic()
    try:
        # Download GTFS-RT
        print(f"Request start : {datetime.now(GTFS_TIMEZONE)}")
        
        
        response = requests.get(GTFS_URL, timeout=30)
        response.raise_for_status()
        print(f"Response end  : {datetime.now(GTFS_TIMEZONE)}")

        # Download timestamp 
        download_dt = datetime.now(GTFS_TIMEZONE)

        # Parse protobuf
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)

        # Feed generation timestamp (Unix -> datetime)
        header_ts = feed.header.timestamp
        feed_dt = datetime.fromtimestamp(header_ts, GTFS_TIMEZONE)

        # Create filename
        filename = f"{feed_dt:%Y%m%d_%H%M%S}_dl{download_dt:%H%M%S}.pb"


        # Save file
        if STORAGE == "s3":
            
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=f"gtfs_rt/{filename}",
                Body=response.content
            )

        elif STORAGE == "local":
            (SAVE_DIR / filename).write_bytes(response.content)

        else:
            raise ValueError(
                f"Unknown STORAGE: {STORAGE}"
            )
        
        elapsed = time.monotonic() - loop_start
        print(f"Elapsed time : {elapsed:.2f}s")

        print(
            f"Saved in {STORAGE}: {filename} "
            f"(Feed={feed_dt:%Y-%m-%d %H:%M:%S}, "
            f"Response size: {len(response.content) / 1024 / 1024:.2f} MB,"
            f"Entities: {len(feed.entity)}, "
            f"Download={download_dt:%Y-%m-%d %H:%M:%S})"
            )
        
        # sleep_time calculation    
        sleep_time = max(0, INTERVAL - elapsed)
        time.sleep(sleep_time)

        

    except Exception as e:
        print(f"Error: {e}")


    
    


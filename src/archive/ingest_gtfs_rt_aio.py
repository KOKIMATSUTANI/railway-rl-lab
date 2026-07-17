from pathlib import Path
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

import aiohttp
from google.transit import gtfs_realtime_pb2

import traceback

# ==========================
# Settings
# ==========================
URL = "https://realtime.gtfs.de/realtime-free.pb"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAVE_DIR = PROJECT_ROOT / "data" / "raw" / "gtfs_rt"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

BERLIN = ZoneInfo("Europe/Berlin")

END_TIME = datetime(
    2026, 6, 30, 9, 46, 0,
    tzinfo=BERLIN
)

INTERVAL = 10  # seconds

# 最大同時ダウンロード数
MAX_CONCURRENT = 3
semaphore = asyncio.Semaphore(MAX_CONCURRENT)


async def download_feed(session: aiohttp.ClientSession):
    """Download one GTFS-RT feed."""

    async with semaphore:

        try:
            download_dt = datetime.now(BERLIN)

            headers = {
                 "User-Agent": "gtfs-collector/1.0" 
                }
            
            async with session.get(URL, headers=headers) as response:
                response.raise_for_status()
                content = await response.read()

            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(content)

            header_ts = feed.header.timestamp
            feed_dt = datetime.fromtimestamp(header_ts, BERLIN)

            filename = (
                SAVE_DIR
                / f"{feed_dt:%Y%m%d_%H%M%S}_dl{download_dt:%H%M%S}.pb"
            )

            filename.write_bytes(content)

            print(
                f"Saved: {filename.name} "
                f"(Feed={feed_dt:%Y-%m-%d %H:%M:%S}, "
                f"Download={download_dt:%Y-%m-%d %H:%M:%S})"
            )

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
        
        finally:
            print("=== GTFS-RT ingestion finished ===")



async def scheduler():

    timeout = aiohttp.ClientTimeout(total=30)

    async with aiohttp.ClientSession(timeout=timeout) as session:

        tasks = []

        while datetime.now(BERLIN) < END_TIME:

            task = asyncio.create_task(
                download_feed(session)
            )
            tasks.append(task)

            await asyncio.sleep(INTERVAL)

        # 全タスク終了待ち
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(scheduler())
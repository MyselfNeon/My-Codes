import asyncio
import logging
import aiohttp

# Configuration variables
KEEP_ALIVE_URL = "https://your-app-url.com" # Replace with your URL
KEEP_ALIVE_INTERVAL = 300 # Ping every 5 minutes
KEEP_ALIVE_TIMEOUT = 15

async def keep_alive():
    """Background task to ping the web server and prevent sleeping."""
    if not KEEP_ALIVE_URL:
        logging.warning("🌐 URL not set. Keep-alive disabled")
        return

    timeout = aiohttp.ClientTimeout(total=KEEP_ALIVE_TIMEOUT)
    first_ping_done = False

    while True:
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(KEEP_ALIVE_URL) as resp:
                    if not first_ping_done:
                        if resp.status == 200:
                            logging.info("✅ First ping OK. Keep-alive running.")
                        else:
                            logging.warning(f"⚠️ First ping status: {resp.status}")
                        first_ping_done = True
        except Exception as e:
            if not first_ping_done:
                logging.error(f"❌ First ping failed: {e}")
                first_ping_done = True
            else:
                logging.error(f"❌ Error: {e}")

        await asyncio.sleep(KEEP_ALIVE_INTERVAL)

def start_keep_alive():
    """Starts the keep-alive task. Call this in your main async function before starting the bot."""
    asyncio.create_task(keep_alive())

import asyncio
import logging
from config import Config
from monitor import PolygonMonitor
from alerts import TelegramAlerter

logging.basicConfig(level=logging.INFO)

async def main():
    config = Config('ETH_monitor/config.yaml')
    monitor = PolygonMonitor(config)
    alerter = TelegramAlerter(config)

    async for alert in monitor.monitor():
        logging.info(f"Alert: {alert}")
        await alerter.send_alert(alert)

if __name__ == "__main__":
    asyncio.run(main())

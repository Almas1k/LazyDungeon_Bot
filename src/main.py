import asyncio
import sys

from loguru import logger

from src.di.container import di


async def main():
    logger.remove()
    logger.add(sys.stdout)
    try:
        await di.player_bot().run()

    finally:
        await di.session_manager().disconnect()
        logger.info("end")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
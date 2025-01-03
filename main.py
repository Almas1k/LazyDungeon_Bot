import asyncio
import sys


from loguru import logger
from src import config

#from src.di.container import di

from src.presentation.bots.player_bot.bot import PlayerBot
from aiogram import Bot, Dispatcher

async def main():
    logger.remove()
    logger.add(sys.stdout)
    bot = Bot(config.PLAYER_BOT_TOKEN)
    dispatcher = Dispatcher()
    player_bot = PlayerBot(bot, dispatcher)
    try:
        await player_bot.run()

    finally:
        #await di.session_manager().disconnect()
        logger.info("end")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
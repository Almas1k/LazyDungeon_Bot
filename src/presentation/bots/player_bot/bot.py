from logging import exception

from aiogram import Dispatcher
from loguru import logger


class PlayerBot:
    def __init__(self):
        pass

    async def run(self):
        try:
            Dispatcher.include_router()
            await Dispatcher.start_polling()
        except exception as e:
            logger.warning(e)

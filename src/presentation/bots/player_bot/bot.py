from logging import exception

from aiogram import Dispatcher, Bot
from loguru import logger

from src.presentation.bots.bot import BaseBot
from src.presentation.bots.player_bot.handlers import handler


class PlayerBot(BaseBot):
    def __init__(self, bot: Bot, dp: Dispatcher):
        super().__init__(bot, dp)

    async def run(self):
        try:
            self.dp.include_router(handler.router)
            await self.dp.start_polling(self.bot)
        except exception as e:
            logger.warning(e)

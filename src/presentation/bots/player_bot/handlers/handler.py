import asyncio
import time
import random

from aiogram import Router
from aiogram.filters import CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.data.services.player_service import PlayerService

router = Router()
player_service: PlayerService

@router.message(CommandStart())
async def handler(msg: Message, state: FSMContext, command: CommandObject):
    answer_msg = await msg.answer("Инициализация...")
    loading_percent = 0
    loading_percent += random.randint(11, 22)
    while loading_percent < 100:
        await asyncio.sleep(1.6)
        await answer_msg.edit_text(f"Инициализация {loading_percent}%")
        loading_percent += random.randint(11, 22)

    await asyncio.sleep(2)
    await answer_msg.edit_text(f"Инициализировано 100%")
    pass

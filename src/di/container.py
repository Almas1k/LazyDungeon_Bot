from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dependency_injector import containers, providers
from dependency_injector.providers import Factory

from src.data.db.session_manager import SessionManager
from src.data.services.player_service import PlayerService
from src.data.services.user_state_service import UserStateService
from src.presentation.user_state_storage import UserStateStorage


def player_handlers__inject():
    from src.presentation.bots.player_bot.handlers import handler
    handler.player_service = di.player_service()


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # DataBase providers
    session_manager = providers.Singleton(
        SessionManager,
        url=config.DB_URL,
    )

    #Services providers
    player_service = providers.Factory(
        PlayerService,
        session_manager=session_manager,
    )

    user_state_service = providers.Factory(
        UserStateService,
        session_manager=session_manager,
    )

    #Presentation layer
    user_state_storage = providers.Factory(
        UserStateStorage,
        user_state_service=user_state_service,
    )

    dp = providers.Factory(
        Dispatcher,
        storage=user_state_storage,
    )

    bot_for_player = providers.Factory(
        Bot,
        token=config.PLAYER_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )



di = Container()
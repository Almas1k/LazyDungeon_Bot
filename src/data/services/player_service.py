from src.data.db.session_manager import SessionManager


class PlayerService:
    def __init__(self, session_manager: SessionManager):
        self.__session_manager = session_manager


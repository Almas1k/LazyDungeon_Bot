from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class SessionManager:
    def __init__(self, url:str):
        logger.info(url)
        self.engine = create_async_engine(url)
        self.get_session = async_sessionmaker(self.engine)
        logger.info(f"Session Manager connected.")

    async def disconnect(self):
        await self.engine.dispose()
        logger.info("Session Manager disconnected")


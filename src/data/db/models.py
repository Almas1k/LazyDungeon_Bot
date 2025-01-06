from sqlalchemy import BIGINT, JSON, DECIMAL, ForeignKey, VARCHAR
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class UserStateOrm(Base):
    __tablename__ = "user_state"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    bot_id: Mapped[int] = mapped_column(BIGINT)
    user_id: Mapped[int] = mapped_column(BIGINT)
    chat_id: Mapped[int] = mapped_column(BIGINT)
    state: Mapped[str] = mapped_column(nullable=True)
    data: Mapped[dict] = mapped_column(JSON)

class PlayerOrm(Base):
    __tablename__ = "player"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    dungeon_id: Mapped[int] = mapped_column(nullable=False)

class DungeonOrm(Base):
    __tablename__ = "dungeon"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    property_id: Mapped[int] = mapped_column()
    object_id: Mapped[int] = mapped_column()

class PropertyOrm(Base):
    __tablename__ = "property"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

class ObjectOrm(Base):
    __tablename__ = "object"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
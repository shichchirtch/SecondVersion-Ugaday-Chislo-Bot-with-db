from sqlalchemy import (Integer, String, ForeignKey)
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import relationship, DeclarativeBase, sessionmaker, Mapped, mapped_column
from config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # tg user id
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    total_games: Mapped[int] = mapped_column(Integer, default=0)
    wins: Mapped[int] = mapped_column(Integer, default=0)


class Game(Base):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(Integer, unique=True)  # tg user id
    secret_number: Mapped[str] = mapped_column(Integer, default=0)
    attempts: Mapped[int] = mapped_column(Integer, default=5)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


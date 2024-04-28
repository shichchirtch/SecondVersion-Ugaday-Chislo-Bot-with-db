from sqlalchemy import (MetaData, Table, Column,
                        Boolean, TIMESTAMP, create_engine, Integer, String, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship, DeclarativeBase, sessionmaker, Mapped, mapped_column
from sqlalchemy.types import Numeric, SmallInteger, DateTime
from typing import Optional
from datetime import datetime

import sqlalchemy as db

# engine = create_engine('sqlite:///Bot_DB3.db', echo=True)
#
# conn = engine.connect()
# metadata = MetaData()
engine = create_engine("sqlite:///bot_map.db", echo=True, future=True)
# Base.metadata.drop_all(engine)

# Base.metadata.create_all(engine)

manipulator = sessionmaker(engine, future=True)
Base = declarative_base()
metadata = Base.metadata
# metadata.drop_all(engine)
class General(Base):
    __tablename__ = 'users'
    index: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    id: Mapped[int] = mapped_column(Integer)  # tg user id
    user_name: Mapped[str] = mapped_column(String(200), nullable=False)
    in_game: Mapped[int] = mapped_column(Integer, default=0)
    secret_number: Mapped[str] = mapped_column(Integer, default=0)
    attempts: Mapped[int] = mapped_column(Integer, default=5)
    total_games: Mapped[int] = mapped_column(Integer, default=0)
    wins: Mapped[int] = mapped_column(Integer, default=0)
    total: Mapped[int] = mapped_column(Integer, default=5)
    game: Mapped[str] = relationship("One_game")


class One_game(Base):
    __tablename__ = 'game'
    index: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    id: Mapped[int] = mapped_column(Integer())
    us_number: Mapped[int] = mapped_column(Integer, nullable=False, unique=False, default=0)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.index'))


metadata.create_all(engine)

# Column('index', Integer(), primary_key=True, autoincrement=True),
# Column('id', Integer()),  # tg user id
# Column('user_name', String(200), nullable=False),
# Column('in_game', Integer(), default=0),
# Column('secret_number', Integer(), default=0),
# Column('attempts', Integer(), default=5),
# Column('total_games', Integer(), default=0),
# Column('wins', Integer(), default=0),
# Column('total', Integer(), default=5), )


# one_game = Table('game', metadata,
#                  Column('index', Integer(), primary_key=True, autoincrement=True),
#                  Column('id', Integer()),
#                  Column('us_number', Integer(), nullable=False),
#                  Column('user_id', ForeignKey(general.columns.id)),)


# metadata.create_all(engine)

# print("\n\n\none game = ", one_game)

# select_query = db.select(one_game.columns.us_number)
# select_results = conn.execute(select_query)
# needed_data_from_game_table = select_results.fetchall()
# print('\n\n\nneeded_data_from_game_table   ', needed_data_from_game_table )
# tuple_number = (nuber_from_message,)

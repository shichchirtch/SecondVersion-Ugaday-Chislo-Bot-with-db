from sqlalchemy import (MetaData, Table, Column,
                        Integer, String, create_engine, ForeignKey, )

import sqlalchemy as db
engine = create_engine('sqlite:///Bot_DB3.db', echo=True)

conn = engine.connect()
metadata = MetaData()
# sql = text(f'DROP TABLE IF EXISTS game;')
# conn.execute(sql)
# conn.commit()
# print("basa deleted")
general = Table('users', metadata,
                Column('index', Integer(), primary_key=True, autoincrement=True),
                Column('id', Integer()), # tg user id
                Column('user_name', String(200), nullable=False),
                Column('in_game', Integer(), default=0),
                Column('secret_number', Integer(), default=0),
                Column('attempts', Integer(), default=5),
                Column('total_games', Integer(), default=0),
                Column('wins', Integer(), default=0),
                Column('total', Integer(), default=5), )
#
one_game = Table('game', metadata,
                 Column('index', Integer(), primary_key=True, autoincrement=True),
                 Column('id', Integer()),
                 Column('us_number', Integer(), nullable=False),
                 Column('user_id', ForeignKey(general.columns.id)),)


metadata.create_all(engine)

# print("\n\n\none game = ", one_game)

# select_query = db.select(one_game.columns.us_number)
# select_results = conn.execute(select_query)
# needed_data_from_game_table = select_results.fetchall()
# print('\n\n\nneeded_data_from_game_table   ', needed_data_from_game_table )
# tuple_number = (nuber_from_message,)

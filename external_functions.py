import sqlalchemy as db
from sqlalchemy import insert
from bot_base import conn
from random import randint

def insert_new_user_in_ganeral_table(table: db.Table, user_tg_id: int, name:str):
    temp_data = db.select(table).where(table.columns.id == user_tg_id)
    select_all_results = conn.execute(temp_data)
    needed_data = select_all_results.one_or_none()
    if not needed_data:
        insertion_query = insert(table).values(id=user_tg_id, user_name=name)
        conn.execute(insertion_query)
        conn.commit()
    else:
        update_query = db.update(table).where(table.columns.id == user_tg_id).values(
            wins=0, total_games=0, secret_number=0, in_game=0, attempts=5)
        conn.execute(update_query)
        conn.commit()

def verify_that_user_into_general(table: db.Table, user_tg_id: int):
    temp_data = db.select(table).where(table.columns.id == user_tg_id)
    select_all_results = conn.execute(temp_data)
    return select_all_results.one_or_none()

def verify_INGAME_status(table: db.Table, user_tg_id: int):
    temp_data = db.select(table.columns.in_game).where(table.columns.id == user_tg_id)
    select_all_results = conn.execute(temp_data)
    return select_all_results.scalar()

def cancel_update(table: db.Table, user_tg_id: int):
    update_query = db.update(table).where(table.columns.id == user_tg_id).values(in_game=0)
    conn.execute(update_query)
    conn.commit()


def choosing_number(table: db.Table, user_tg_id: int):
    update_query = (db.update(table).where(table.columns.id == user_tg_id).values(in_game=1,
                                                                                   secret_number = randint(1, 100)))
    conn.execute(update_query)
    conn.commit()

def get_secret_number(table: db.Table, user_tg_id: int):
    select_query = db.select(table.columns.secret_number).where(table.columns.id == user_tg_id)
    select_results = conn.execute(select_query)
    needed_data_from_first_table = select_results.scalar()
    if needed_data_from_first_table:
        return needed_data_from_first_table
    return "This Name Does Not Exist"

def update_after_user_wins(table: db.Table, user_tg_id: int):
    select_query = db.select(table.columns.wins).where(table.columns.id == user_tg_id)
    select_results = conn.execute(select_query)
    wins_number = select_results.scalar()+1
    select_query = db.select(table.columns.total_games).where(table.columns.id == user_tg_id)
    select_results = conn.execute(select_query)
    total_game_number = select_results.scalar() + 1
    update_query = db.update(table).where(table.columns.id == user_tg_id).values(
        wins=wins_number, total_games=total_game_number, secret_number=0, in_game=0 )
    conn.execute(update_query)
    conn.commit()


def minus_one_attempt(table: db.Table, user_tg_id: int):
    select_query = db.select(table.columns.attempts).where(table.columns.id == user_tg_id)
    select_results = conn.execute(select_query)
    att_number = select_results.scalar() - 1
    update_query = db.update(table).where(table.columns.id == user_tg_id).values(attempts=att_number)
    conn.execute(update_query)
    conn.commit()

def check_attempts_lost_number(table: db.Table, user_tg_id: int):
    select_query = db.select(table.columns.attempts).where(table.columns.id == user_tg_id)
    select_results = conn.execute(select_query)
    att_number = select_results.scalar()
    if att_number == 0:
        return True
    return False

def user_lost(table: db.Table, user_tg_id: int):
    select_query = db.select(table.columns.total_games).where(table.columns.id == user_tg_id)
    select_results = conn.execute(select_query)
    total_game_number = select_results.scalar() + 1
    update_query = db.update(table).where(table.columns.id == user_tg_id).values(
         total_games=total_game_number, secret_number=0, in_game=0, attempts=5)
    conn.execute(update_query)
    conn.commit()

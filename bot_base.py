

# with sqlite3.connect('mybase.db') as db:
#     cursor = db.cursor()
#     query = """CREATE TABLE IF NOT EXISTS users
#     (user_id INTEGER,
#      user_name TEXT,
#      in_game NULL,
#      secret_number NULL,
#      attempts INTEGER,
#      total_games INTEGER,
#      wins INTEGER,
#      total INTEGER,
#      game_list TEXT,
#      bot_list TEXT,
#      set_attempts TEXT,
#      user_number TEXT,
#      bot_taily TEXT,
#      bot_win INTEGER,
#      bot_pobeda INTEGER,
#      start_time NULL)"""
#     cursor.execute(query)
#     db.commit()
#

import sqlite3, aiosqlite
with sqlite3.connect('mybase7.db') as db:   # Так создаётся БД\\ Имя должно быть уникальным !
    print("Запрос к БД")
    cursor = db.cursor()  #  В таблице будет 3 колонки
    query = """CREATE TABLE IF NOT EXISTS users 
    (user_id INTEGER,  
     user_name TEXT, 
     in_game INTEGER)"""
    cursor.execute(query)
    db.commit()  # Мэнеджер контекста  -  with - сам закроет БД
    print("table is created")


async def add_user(user_id, user_name, in_game):
    print("Add users works ")
    connect = await aiosqlite.connect('mybase7.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    check_user = await check_user.fetchone()
    print(check_user)
    if check_user is None:
        print(f"{user_name} ещё не в таблице")
        await cursor.execute('INSERT INTO users (user_id, user_name, in_game) VALUES (?, ?, ?)',
                         (user_id, user_name, in_game ))
    await connect.commit()
    await cursor.close()
    await connect.close()
    print('add finish')

# async def add_user(user_id, user_name, in_game, secret_number,
#                    attempts, total_games, wins, total, game_list, bot_list, set_attempts,
#                    user_number, bot_taily, bot_win, bot_pobeda, start_time):
#     connect = await aiosqlite.connect('mybase.db')
#     cursor = await connect.cursor()
#     check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
#     check_user = await check_user.fetchone()
#     if check_user is None:
#         await cursor.execute('INSERT INTO users (user_id, user_name, in_game, secret_number,'
#                    'attempts, total_games, wins, total, game_list, bot_list, set_attempts,'
#                    'user_number, bot_taily, bot_win, bot_pobeda, start_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
#                              (user_id, user_name, in_game, secret_number,
#                    attempts, total_games, wins, total, game_list, bot_list, set_attempts,
#                    user_number, bot_taily, bot_win, bot_pobeda, start_time))
#         await connect.commit()
#     await cursor.close()
#     await connect.close()


user_belongnes={
            'user_name': '',
            'in_game': False,
            'secret_number': None,
            'attempts': 5,
            'total_games': 0,
            'wins': 0,
            'total': 5,
            'game_list': [],
            'bot_list': [],
            'set_attempts': 'NotSet',
            'user_number': 'setting_data',
            'bot_taily': 'empty',
            'bot_win': False,
            'bot_pobeda': 0,
            'language': 0,
            'start_time': None,
            'chemp': {'count_bot_win': 0, 'count_user_win': 0, 'status': False},
            'chemp_result': 0
        }
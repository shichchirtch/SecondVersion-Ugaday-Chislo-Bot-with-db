from aiogram import Router
from filters import *
from aiogram.filters import Command, CommandStart
from keyboards import *
from lexicon import start_greeding
from loggers import *
from aiogram.types import CallbackQuery, Message
from bot_base import db, add_user
import sqlite3, aiosqlite

command_router = Router()


import time


# Инициализируем роутер уровня модуля
Comand_router = Router()

@command_router.message(CommandStart())
async def process_start_command(message: Message):
    # Логируем старт Бота
    print(f'user {message.chat.first_name} press start')
    user_name = message.chat.first_name


    # # start_time = time.monotonic()
    in_game = 0
    # secret_number = None
    # attempts = 5
    # total_games = 0
    # wins = 0
    # total = 5
    # game_list = 'empty'
    # bot_list = 'empty'
    # set_attempts= 'NotSet'
    # user_number = 'setting_data'
    # bot_taily =  'empty'
    # bot_win = 0
    # bot_pobeda = 0
    # start_time = None
    # await add_user(message.from_user.id,
    #                user_name,
    #                in_game,
    #                secret_number,
    #                attempts,
    #                total_games,
    #                wins,
    #                total,
    #                game_list,
    #                bot_list,
    #                set_attempts,
    #                user_number,
    #                bot_taily,
    #                bot_win,
    #                bot_pobeda,
    #                start_time )

    await add_user(message.from_user.id,
                   user_name,
                   in_game)
    print(message.from_user.id)
    await message.answer(
        f'Привет, {message.chat.first_name} !  \U0001F60A\n {start_greeding}')
    time.sleep(1)
    await message.answer(text='Если хотите установить количество попыток введите число от 1\uFE0F\u20E3 до \U0001f51f\n'
                         'По умолчанию у вас 5\uFE0F\u20E3  попыток',
                         reply_markup=keyboard_attempts)
    std_out_logger.info(f'\nБот запустил {message.chat.first_name}')# print('Only print, when new User start bot') log
    # std_err_logger.info(f'\nСтруктура словаря юзера {users[message.from_user.id]["user_name"]} = {users[message.from_user.id]} ')
    # logger.warning(f'Структура словаря users =  {users}')# pprint(users) # log
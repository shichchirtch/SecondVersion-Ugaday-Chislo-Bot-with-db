from aiogram import Router, F
from filters import *
from keyboards import *
from lexicon import positiv_answer, language_dict, negative_answer
from aiogram.types import  Message, ReplyKeyboardRemove, ContentType
from external_functions import (verify_INGAME_status, choosing_number,
                                verify_that_user_into_general )
                                # get_secret_number,
                                # update_after_user_wins, minus_one_attempt,
                                # check_attempts_lost_number, user_lost)


# from bot_base import General,  engine, One_game
import time


user_router = Router()
@user_router.message(F.content_type != ContentType.TEXT)
async def process_notTEXT_answers(message: Message):
    user_tg_id = message.from_user.id
    user_name = message.chat.first_name
    if verify_INGAME_status(user_tg_id):
        await message.answer(language_dict['wrong sent data'])
    else:
        await message.answer(user_name + language_dict['wrong content type'])

@user_router.message(DATA_IS_NOT_DIGIT(), F.text.lower().in_(positiv_answer))
async def process_positive_answer(message: Message):
    print("posetive works")
    user_tg_id = message.from_user.id
    choosing_number(user_tg_id)
    print('choosing_number works')
    # INSERT_IN_GAME_TABLE(user_tg_id)
    await message.answer(text="Я загадал число, начинайте угадывать !",
                         reply_markup=ReplyKeyboardRemove())

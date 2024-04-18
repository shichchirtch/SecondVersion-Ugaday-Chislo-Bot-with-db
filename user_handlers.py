from aiogram import Router, F
from filters import *
from keyboards import *
from lexicon import LEXICON, positiv_answer, language_dict
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
import aiosqlite
user_router = Router()

@user_router.message(DATA_IS_NOT_DIGIT(), F.text.lower().in_(positiv_answer))
async def process_positive_answer(message: Message):
    userID = message.from_user.id
    # Устанавливаем соединение с базой данных
    connect = await aiosqlite.connect('mybase7.db')
    cursor = await connect.cursor()
    # Обновляем game status
    await cursor.execute('UPDATE users SET in_game = ? WHERE user_id = ?', (1, f'{userID}'))
    # Сохраняем изменения и закрываем соединение
    await connect.commit()
    await connect.close()
    await message.answer(language_dict['new number'],
                             reply_markup=ReplyKeyboardRemove())

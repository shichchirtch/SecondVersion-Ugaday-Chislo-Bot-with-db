from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


path = 'D:\data\Ivan\Programming\Second_Version Ugaday Chislo Bot\.env'


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))














    # Устанавливаем соединение с базой данных
    # connect = await aiosqlite.connect('mybase7.db')
    # cursor = await connect.cursor()
    # # Обновляем game status
    # await cursor.execute('UPDATE users SET in_game = ? WHERE user_id = ?', (1, f'{userID}'))
    # # Сохраняем изменения и закрываем соединение
    # await connect.commit()
    # await connect.close()
    # await message.answer(language_dict['new number'],
    #                          reply_markup=ReplyKeyboardRemove())
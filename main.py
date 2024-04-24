import asyncio
import logging


from aiogram import Bot, Dispatcher
from config import Config, load_config
# import user_handlers
import command_handlers
import user_handlers
from sqlalchemy import text

from keyboards import set_main_menu
# from sqlalchemy import (MetaData, Table, Column,
#                         Integer, String, Text, ForeignKey, create_engine, insert, select, values, text)
# import sqlalchemy as db

# Инициализируем логгер
# logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format='%(filename)s:%(lineno)d #%(levelname)-8s '
    #            '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    # logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()



    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(command_handlers.command_router)
    dp.include_router(user_handlers.user_router)



    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




asyncio.run(main())
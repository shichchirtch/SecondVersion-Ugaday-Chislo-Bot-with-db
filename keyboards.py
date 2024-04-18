from aiogram import Bot
from aiogram.types import BotCommand
from lexicon import LEXICON_COMMANDS
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command,
        description in LEXICON_COMMANDS.items()]

    await bot.set_my_commands(main_menu_commands)

pre_start_button = KeyboardButton(text='/start')

pre_start_clava = ReplyKeyboardMarkup(
    keyboard=[[pre_start_button]],
    resize_keyboard=True,
    input_field_placeholder='Приятного чтения'
)



# создаю конструктор клавиатур
# kb_builder = ReplyKeyboardBuilder()
#Создаю кнопки
start_button_1 = KeyboardButton(text='ДА')
start_button_2 = KeyboardButton(text='НЕТ')
att_button = KeyboardButton(text='Переустановить количество попыток')
schet_button = KeyboardButton(text='Узнать Счёт')

#  Создаю клавиатуру на согласие играть
keyboard1 = ReplyKeyboardMarkup(
    keyboard=[[start_button_1, start_button_2]],
    resize_keyboard=True)

#  создаю кнопки для установки количества попыток
buttons_attempts: list[KeyboardButton] = [KeyboardButton(text=f'{i + 1}') for i in range(10)]

#  создаю клавиатуру установки количества попыток
keyboard_attempts = ReplyKeyboardMarkup(
    keyboard=[buttons_attempts],
    resize_keyboard=True)
#  создаю клавитуру после проигрыша
keyboard_after_fail = ReplyKeyboardMarkup(
    keyboard=[[start_button_1, start_button_2],[att_button],[schet_button]],
    resize_keyboard=True)
#создаю клавиатуру с одной с кнопками Да и Узнать счет.
keyboard_after_saying_NO = ReplyKeyboardMarkup(
    keyboard=[[start_button_1], [schet_button]],
    resize_keyboard=True)

keyboard_for_help = ReplyKeyboardMarkup(
                    keyboard=[[start_button_1, start_button_2],
                              [att_button]],
                    resize_keyboard=True)
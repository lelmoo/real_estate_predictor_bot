from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU
import os
import sys
sys.path.append(os.getcwd())

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text='1')
button_2 = KeyboardButton(text='2')
button_3 = KeyboardButton(text='3')
button_4 = KeyboardButton(text='4')
button_5 = KeyboardButton(text='5')
button_studio = KeyboardButton(text='studio')

button_panel = KeyboardButton(text='панельный')
button_monolit = KeyboardButton(text='монолитный')
button_brick = KeyboardButton(text='кирпичный')
button_brickmonolit = KeyboardButton(text='монолитно-кирпичный')
button_block = KeyboardButton(text='блочный')

button_euro = KeyboardButton(text='евро')
button_design = KeyboardButton(text='дизайнерский')
button_bad = KeyboardButton(text='требует ремонта')
button_cosmetic = KeyboardButton(text='косметический')

button_5_min = KeyboardButton(text='до 5 мин.')
button_6_10 = KeyboardButton(text='6-10 мин.')
button_11_15 = KeyboardButton(text='11-15 мин.')
button_16_20 = KeyboardButton(text='16-20 мин.')
button_21_30 = KeyboardButton(text='21-30 мин.')
button_30 = KeyboardButton(text='от 31 мин.')


rooms_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3],
              [button_4],
              [button_5],
              [button_studio]],
    resize_keyboard=True
)

material_kb = ReplyKeyboardMarkup(
    keyboard=[[button_panel],
              [button_monolit],
              [button_brick],
              [button_brickmonolit],
              [button_block]],
    resize_keyboard=True
)

condition_kb = ReplyKeyboardMarkup(
    keyboard=[[button_euro],
              [button_design],
              [button_bad],
              [button_cosmetic]],
    resize_keyboard=True
)

metro_kb = ReplyKeyboardMarkup(
    keyboard=[[button_5_min],
              [button_6_10],
              [button_11_15],
              [button_16_20],
              [button_21_30],
              [button_30]],
    resize_keyboard=True
)
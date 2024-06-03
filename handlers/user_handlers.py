from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import yes_no_kb, rooms_kb, material_kb, condition_kb, metro_kb
from lexicon.lexicon_ru import LEXICON_RU
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from services.ml import ml_price

class Form(StatesGroup):
    coordinates = State()
    rooms = State()
    material = State()
    year = State()
    floors = State()
    apartment_floor = State()
    apartment_area = State()
    repair = State()
    metro = State()
    kitchen_area = State()


router = Router()
current_state = None


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=types.ReplyKeyboardRemove())


# Обработка координат
@router.message(F.text.regexp((r'^\d{2}\.\d+, \d{2}\.\d+$')))
async def process_coordinates(message: Message, state: FSMContext):
    await state.set_state(Form.coordinates)
    coordinates = message.text.split(',')
    await state.update_data(coords=(float(coordinates[0]), float(coordinates[1])))
    await message.answer(text=LEXICON_RU['coords'], reply_markup=rooms_kb)

# Обработка количества комнат
@router.message(F.text.in_(['1', '2', '3', '4', '5', 'студия']))
async def process_rooms(message: Message, state: FSMContext):
    await state.set_state(Form.rooms)
    await state.update_data(rooms_count=message.text)
    await message.answer(text=LEXICON_RU['rooms'], reply_markup=types.ReplyKeyboardRemove())

# Обработка года постройки
@router.message(F.text.regexp(r'^\d{4}$'))
async def process_year(message: Message, state: FSMContext):
    await state.set_state(Form.year)
    await state.update_data(year=int(message.text))
    await message.answer(text=LEXICON_RU['year'], reply_markup=material_kb)


# Обработка материала здания
@router.message(F.text.in_(['панельный', 'монолитный', 'кирпичный', 'монолитно-кирпичный', 'блочный']))
async def process_material(message: Message, state: FSMContext):
    await state.set_state(Form.material)
    await state.update_data(material=message.text)
    await message.answer(text=LEXICON_RU['material'], reply_markup=types.ReplyKeyboardRemove())


# Обработка площади квартиры
@router.message(F.text.regexp(r'^\d+(\.\d+)?$'))
async def process_apartment_area(message: Message, state: FSMContext):
    await state.set_state(Form.apartment_area)
    await state.update_data(flat_area=float(message.text))
    await message.answer(text=LEXICON_RU['flat_area'], reply_markup=metro_kb)


# Обработка расстояния до метро
@router.message(F.text.in_(['до 5 мин.', '6-10 мин.', '11-15 мин.', '16-20 мин.', '21-30 мин.', 'от 31 мин.']))
async def process_metro(message: Message, state: FSMContext):
    await state.set_state(Form.metro)
    await state.update_data(metro=message.text)
    await message.answer(text=LEXICON_RU['metro'], reply_markup=condition_kb)


# Обработка типа ремонта
@router.message(F.text.in_(['требует ремонта', 'косметический', 'евро', 'дизайнерский']))
async def process_repair(message: Message, state: FSMContext):
    await state.set_state(Form.repair)
    await state.update_data(condition=message.text)
    await message.answer("Предсказание цены...", reply_markup=types.ReplyKeyboardRemove())
    data = await state.get_data()

    # Вызов функции предсказания цены
    price = ml_price(data)

    await message.answer(f"Предсказанная цена: {price} рублей")
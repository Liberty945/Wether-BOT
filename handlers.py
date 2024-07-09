from config import TOKEN_API as bot_token
from aiogram import Bot, Dispatcher, types
from keyboards import get_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from parsing import weather_check

storage = MemoryStorage()


class States(StatesGroup):
    wait = State()


bot = Bot(bot_token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.delete()
    await message.answer('Бот готов к работе', reply_markup=get_keyboard()) #обработка команды старт


@dp.message_handler(lambda message: message.text == 'Узнать погоду') #обработка сообщения
async def cmd_post_start(message: types.Message):
    await message.answer('Введите название города')
    await States.wait.set()


@dp.message_handler(lambda message: message.text.isdigit(), state=States.wait)
async def check_int(message: types.Message):
    await message.answer('Введите название города без цифр')


@dp.message_handler(lambda message: not message.text.isdigit(), state=States.wait)  #вывод информации о погоде
async def check_city(message: types.Message, state: FSMContext):
    city_input = str(message.text)
    weather_info = weather_check(f'{city_input} погода')
    await message.answer(f'Вот инфомация о погоде: {weather_info}', reply_markup=get_keyboard())
    await state.finish()

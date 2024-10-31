from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


# Определение состояний
class Form(StatesGroup):
    name = State()  # Состояние для имени
    age = State()  # Состояние для возраста


# Команда /start – инициирует диалог и запускает первое состояние
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await Form.name.set()
    await message.reply("Привет! Как тебя зовут?")


# Получаем имя и переходим к следующему состоянию
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)  # Сохраняем имя
    await Form.next()  # Переход к следующему состоянию
    await message.reply("Сколько тебе лет?")


# Получаем возраст, завершаем машину состояний и выводим результат
@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))  # Сохраняем возраст
    data = await state.get_data()
    await message.reply(f"Приятно познакомиться, {data['name']}! Тебе {data['age']} лет.")
    await state.finish()  # Завершаем машину состояний


# Обработка ввода неверного значения для возраста
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    await message.reply("Пожалуйста, введи число для возраста.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

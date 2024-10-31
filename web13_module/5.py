from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Создаем клавиатуру с кнопками для выбора категории
def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(KeyboardButton("Погода"), KeyboardButton("Новости"), KeyboardButton("Шутка"))
    keyboard.row(KeyboardButton("Погода"), KeyboardButton("Шутка"))
    keyboard.row(KeyboardButton("Новости"))
    # keyboard.row(KeyboardButton("Шутка"))
    return keyboard


# Команда /start – отправляет сообщение с кнопками категорий
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.reply("Привет! Выберите категорию:", reply_markup=get_main_keyboard())


# Обработка нажатия кнопки "Погода"
@dp.message_handler(lambda message: message.text == "Погода")
async def handle_weather(message: types.Message):
    await message.reply("Сегодня солнечно, температура около 25°C ☀️")


# Обработка нажатия кнопки "Новости"
@dp.message_handler(lambda message: message.text == "Новости")
async def handle_news(message: types.Message):
    await message.reply("Последние новости: открытие нового парка в центре города!")


# Обработка нажатия кнопки "Шутка"
@dp.message_handler(lambda message: message.text == "Шутка")
async def handle_joke(message: types.Message):
    await message.reply("Почему программисты не любят природу? Слишком много багов! 😄")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

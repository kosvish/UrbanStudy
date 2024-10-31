from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import API_TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Хендлер для команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    print("Привет! Это команда /start")


# Хендлер для сообщения "Urban"
@dp.message_handler(lambda message: message.text == "Urban")
async def urban_message(message: types.Message):
    print('Best University')


# Общий хендлер для всех сообщений
@dp.message_handler()
async def all_messages(message: types.Message):
    print("Вы отправили сообщение: " + message.text)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

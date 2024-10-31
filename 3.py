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
    await message.answer("***Рады вас видеть*** в нашем *боте*!", parse_mode="Markdown")


# Хендлер для сообщения "Urban"
@dp.message_handler(lambda message: message.text == "Urban")
async def urban_message(message: types.Message):
    await message.answer('Best University')


@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    await message.answer_photo(
        photo="https://static.tildacdn.com/tild6536-3061-4239-b266-643564363961/photo_2024-01-18_145.jpeg",
        caption="Вот ваша картинка!")


# Хендлер для любого сообщения (эхо-бот)
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer(f"Вы отправили сообщение: {message.text}")


@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    photos = message.photo
    print(len(photos))
    for photo in photos:
        print(photo.__dict__)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

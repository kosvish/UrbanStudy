from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Функция для создания inline-клавиатуры
def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_yes = InlineKeyboardButton("Да", callback_data="answer_yes")
    button_no = InlineKeyboardButton("Нет", callback_data="answer_no")
    keyboard.add(button_yes, button_no)
    return keyboard


# Команда /start – отправляет сообщение с inline-кнопками
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.reply("Ты хочешь продолжить?", reply_markup=get_inline_keyboard())


# Обработка нажатия кнопки "Да"
@dp.callback_query_handler(lambda c: c.data == 'answer_yes')
async def process_callback_yes(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback (для закрытия "часиков")
    await bot.send_message(callback_query.from_user.id, "Отлично, продолжим!")


# Обработка нажатия кнопки "Нет"
@dp.callback_query_handler(lambda c: c.data == 'answer_no')
async def process_callback_no(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Хорошо, завершаем.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

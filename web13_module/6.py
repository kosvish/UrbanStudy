from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# target_NotCoin_20

# Функция для создания inline-клавиатуры
def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup()
    button_yes = InlineKeyboardButton("Да", callback_data="answer_yes")
    button_no = InlineKeyboardButton("Нет", callback_data="answer_no")
    button_yandex = InlineKeyboardButton("сайт яндекса", url='https://ya.ru')
    keyboard.add(button_yes, button_no, button_yandex)
    return keyboard


# Команда /start – отправляет сообщение с inline-кнопками
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.reply("Ты хочешь продолжить?", reply_markup=get_inline_keyboard())


# Обработка нажатия кнопки "Да"
# @dp.callback_query_handler(lambda callback: callback.data == 'answer_yes')
# async def process_callback_yes(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)  # Отвечаем на callback (для закрытия "часиков")
#     await callback_query.answer("Отлично, продолжим!")
#     #await bot.send_message(callback_query.from_user.id, "Отлично, продолжим!")
#
#
# # Обработка нажатия кнопки "Нет"
# @dp.callback_query_handler(lambda callback: callback.data == 'answer_no')
# async def process_callback_no(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, "Хорошо, завершаем.")


@dp.callback_query_handler(lambda callback: True)
async def get_callbacks(callback_query: types.CallbackQuery):
    if callback_query.data == 'answer_no':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Хорошо, завершаем.")

    if callback_query.data == 'answer_yes':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Хорошо, продолжаем.")

    if callback_query.data.startswith('target_'):
        # target_NotCoin_20
        a = callback_query.data.split('_')
        print(a[1])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

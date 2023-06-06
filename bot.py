import logging
from aiogram import Bot, Dispatcher, executor, types
import inline_keyboard
import messages
from settings import API_TOKEN, city_list, zodiak, banks



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=API_TOKEN)

# Диспетчер
dp = Dispatcher(bot)


# запускаем меню бота
@dp.message_handler(commands=['start'])
async def start_mybot(message: types.Message):
    logging.info(message)
    await message.answer(text=messages.start_bot(),
                         reply_markup=inline_keyboard.menu())

# хендлер погоды
@dp.message_handler(text='Погода 🌤')
async def weather_menu(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.select_city(),
                         reply_markup=inline_keyboard.btn_all_city())

# выбор города
@dp.message_handler(text=city_list)
async def weather_select_city(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.weather_get_city(callback.text))

# хендлер гороскопа
@dp.message_handler(text='Гороскоп ♓️')
async def horoscope_menu(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.zodiak_select(),
                         reply_markup=inline_keyboard.btn_all_zodiak())

# выбор знака зодиака
@dp.message_handler(text=zodiak)
async def horoscope_select_zodiak(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.select_data(),
                         reply_markup=inline_keyboard.select_date_zodiak(callback.text))

# выбор даты гороскопа
@dp.callback_query_handler(inline_keyboard.zodiak_callback.filter())
async def horoscope_select_date(callback: types.CallbackQuery, callback_data: dict):
    logging.info(callback_data)
    zodiak = callback_data['name']
    date = callback_data['select_date']
    await bot.send_message(chat_id=callback.message.chat.id, text=messages.horoscope(zodiak, date),
                         reply_markup=inline_keyboard.menu())

# хендлер курса валют
@dp.message_handler(text='Курс валют 🏦')
async def horoscope_menu(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.bank_select(),
                         reply_markup=inline_keyboard.btn_all_bank())

# выбор банка
@dp.message_handler(text=banks)
async def horoscope_select_zodiak(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.bank_data_request(callback.text))

# хендлер статистики агрессии с minfin
@dp.message_handler(text='Агрессия против Украины')
async def horoscope_menu(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.war_info(),
                         reply_markup=inline_keyboard.menu())

# хендлер топа криптовалюты за сутки
@dp.message_handler(text='Топ криптовалют 💰')
async def horoscope_menu(callback: types.CallbackQuery):
    logging.info(callback)
    await callback.answer(text=messages.cripta(),
                         reply_markup=inline_keyboard.menu())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

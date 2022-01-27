import telebot
from telebot import types
from basic import Horoscope, Weather, ExchangeRates

token='10XXXXXX29:AAFs7Z2qQXXXXXXXXXXXXXXXXXXXXgEXCxpA'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    msg = bot.send_message(message.chat.id, "Вас приветствует Бот")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Курс валют', 'Погода']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Гороскоп', 'Новости']])
    bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)


def name(message):
    if message.text == 'Гороскоп':
        msg = bot.send_message(message.chat.id, "Вы выбрали 'Гороскоп'")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['♈ Овен', '♉ Телец', '♊ Близнецы']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['♋ Рак', '♌ Лев', '♍ Дева']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['♎ Весы', '♏ Скорпион', '♓ Рыбы']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['♐ Стрелец', '♑ Козерог', '♒ Водолей']])
        bot.send_message(message.chat.id, 'Выберите "Зодиак"', reply_markup=keyboard)
        bot.register_next_step_handler(msg, zodiak)

    elif message.text == 'Погода':
        msg = bot.send_message(message.chat.id, "Вы выбрали 'Погоду'")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Одесса', 'Днепр', 'Винница']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Львов', 'Черновцы', 'Николаев']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Житомир', 'Ужгород', 'Луганск']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Запорожье', 'Черкассы', 'Донецк']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полтава', 'Хмельницкий', 'Луцк']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тернополь', 'Харьков', 'Херсон']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Ровно', 'Сумы', 'Киев', 'Чернигов']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Кропивницкий', 'Ивано-Франковск']])
        bot.send_message(message.chat.id, 'Выберите город', reply_markup=keyboard)
        bot.register_next_step_handler(msg, all_weather)
    
    elif message.text == 'Курс валют':
        msg = bot.send_message(message.chat.id, 'Вы вибрали "Курс валют"')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['ОЩАД', 'АЛЬФА', 'ПУМБ']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['ПIВДЕННИЙ', 'MTB', 'НБУ']])
        bot.send_message(message.chat.id, 'Выберите БАНК', reply_markup=keyboard)
        bot.register_next_step_handler(msg, all_curr)

    elif message.text == 'Новости':
        msg = bot.send_message(message.chat.id, 'В разработке')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В главное меню']])
        bot.send_message(message.chat.id, 'Выберите другой раздел', reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)


# Погода
def all_weather(message):
    weather = Weather()
    res_weather = weather.get_city(message.text)
    msg = bot.send_message(message.chat.id, f"Погода в г. {message.text}")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert) for advert in ['В главное меню']])
    bot.send_message(message.chat.id, f'{res_weather}', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)


# Гороскоп
def zodiak(message):
    global zodiak_name
    zodiak_name = message.text
    msg = bot.send_message(message.chat.id, f'Вы вибрали {message.text}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert) for advert in ['Вчера', 'Сегодня', 'Завтра']])
    bot.send_message(message.chat.id, 'Выберите дату', reply_markup=keyboard)
    bot.register_next_step_handler(msg, horoscopes)


# Курсы валют
def all_curr(message):
    exchange_rates = ExchangeRates()
    if message.text == 'НБУ':
        msg = bot.send_message(message.chat.id, exchange_rates.nbu_bank())

    if message.text == 'MTB':
        msg = bot.send_message(message.chat.id, exchange_rates.mtb_bank())

    if message.text == 'АЛЬФА':
        msg = bot.send_message(message.chat.id, exchange_rates.alfa_bank())

    if message.text == 'ОЩАД':
        msg = bot.send_message(message.chat.id, exchange_rates.oschad_bank())

    if message.text == 'ПУМБ':
        msg = bot.send_message(message.chat.id, exchange_rates.pumb_bank())

    if message.text == 'ПIВДЕННИЙ':
        msg = bot.send_message(message.chat.id, exchange_rates.pivden_bank())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert) for advert in ['В главное меню']])
    bot.send_message(message.chat.id, '🧐', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)


def horoscopes(message):
    horoscope = Horoscope()
    msg = bot.send_message(message.chat.id, f'Ваш гороскоп на {message.text}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert) for advert in ['В главное меню']])
    bot.send_message(message.chat.id, horoscope.search(zodiak_name, message.text), reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)



if __name__ == '__main__':
    print("[+] Start BOT")
    bot.polling(none_stop=True, interval=0)

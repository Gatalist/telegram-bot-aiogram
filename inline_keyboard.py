from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def btn_all_city():
    all_city = ReplyKeyboardMarkup(resize_keyboard=True)
    all_city.add(
        InlineKeyboardButton(text='Одесса'),
        InlineKeyboardButton(text='Киев'),
        InlineKeyboardButton(text='Винница')
    )
    all_city.add(
        InlineKeyboardButton(text='Луцк'),
        InlineKeyboardButton(text='Днепр'),
        InlineKeyboardButton(text='Донецк')
    )
    all_city.add(
        InlineKeyboardButton(text='Житомир'),
        InlineKeyboardButton(text='Ужгород'),
        InlineKeyboardButton(text='Запорожье')
    )
    all_city.add(
        InlineKeyboardButton(text='Ивано-Франковск'),
        InlineKeyboardButton(text='Кропивницкий'),
        InlineKeyboardButton(text='Луганск')
    )
    all_city.add(
        InlineKeyboardButton(text='Львов'),
        InlineKeyboardButton(text='Николаев'),
        InlineKeyboardButton(text='Тернополь')
    )
    
    all_city.add(
        InlineKeyboardButton(text='Полтава'),
        InlineKeyboardButton(text='Ровно'),
        InlineKeyboardButton(text='Сумы')
    )
    all_city.add(
        InlineKeyboardButton(text='Харьков'),
        InlineKeyboardButton(text='Херсон'),
        InlineKeyboardButton(text='Хмельницкий')
    )
    all_city.add(
        InlineKeyboardButton(text='Черкассы'),
        InlineKeyboardButton(text='Чернигов'),
        InlineKeyboardButton(text='Черновцы')
    )

    return all_city


def menu():
    menu_list = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_list.add(
        InlineKeyboardButton("Погода 🌤"),
        InlineKeyboardButton("Гороскоп ♓️"),
    )
    menu_list.add(
        InlineKeyboardButton("Курс валют 🏦"),
        InlineKeyboardButton("Топ криптовалют 💰"),
    )
    menu_list.add(
        InlineKeyboardButton("Война 🔥")
    )

    return menu_list


def btn_all_zodiak():
    btn_all_zodiak = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_all_zodiak.add(
        InlineKeyboardButton("♈ Овен"),
        InlineKeyboardButton("♉ Телец"),
        InlineKeyboardButton("♊ Близнецы"),
    )
    btn_all_zodiak.add(
        InlineKeyboardButton("♋ Рак"),
        InlineKeyboardButton("♍ Дева"),
        InlineKeyboardButton("♎ Весы"),
        
    )
    btn_all_zodiak.add(
        InlineKeyboardButton("♏ Скорпион"),
        InlineKeyboardButton("♐ Стрелец"),
        InlineKeyboardButton("♑ Козерог"),
    )

    btn_all_zodiak.add(
        InlineKeyboardButton("♒ Водолей"),
        InlineKeyboardButton("♓ Рыбы"),
        InlineKeyboardButton("♌ Лев"),
    )

    return btn_all_zodiak


zodiak_callback = CallbackData('name_template', 'name', 'select_date')
def select_date_zodiak(name_zodiak):
    menu_list = InlineKeyboardMarkup(resize_keyboard=True)
    print(f"click: open func select_date_zodiak - data {name_zodiak}")
    menu_list.add(
        InlineKeyboardButton("Вчера", callback_data=zodiak_callback.new(name=name_zodiak, select_date='Вчера')),
        InlineKeyboardButton("Сегодня", callback_data=zodiak_callback.new(name=name_zodiak, select_date='Сегодня')),
        InlineKeyboardButton("Завтра", callback_data=zodiak_callback.new(name=name_zodiak, select_date='Завтра')),
    )
    return menu_list


def btn_all_bank():
    btn_all_bank = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_all_bank.add(
        InlineKeyboardButton("Mono"),
        InlineKeyboardButton("ПУМБ"),
        InlineKeyboardButton("MTB Банк"),
    )
    btn_all_bank.add(
        InlineKeyboardButton("АЛЬФА-БАНК"),
        InlineKeyboardButton("Південний"),
        InlineKeyboardButton("Ощад Банк"),
    )
    btn_all_bank.add(
        InlineKeyboardButton("НБУ курс"),
    )

    return btn_all_bank


def btn_war():
    btn_all_war = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_all_war.add(
        InlineKeyboardButton("Последняя статистике"),
    )

    return btn_all_war


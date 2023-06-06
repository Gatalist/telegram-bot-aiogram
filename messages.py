from basic import ExchangeRates, Weather, Horoscope, RussianInvading, BinaceCoinRating


def start_bot():
    return "Приветствую, что тебя интересует?"

def loading():
    return f"В разработке"

def select_city() -> str:
    return f'Выберите город'


def weather_get_city(city_name) -> str:
    return Weather().get_city(city_name)


def zodiak_select() -> str:
   return f'Выберите знак зодиака'


def select_data() -> str:
    return f'Выберите дату'


def horoscope(name, data) -> str:
   return Horoscope().search(name, data)


def bank_select():
    return f'Выберите банк'

def bank_data_request(name):
    rates = ExchangeRates()
    print(name)

    if name == "НБУ курс":
        return rates.nbu_bank()
    
    if name == "Південний":
        return rates.pivden_bank()

    if name == "MTB Банк":
        return rates.mtb_bank()
    
    if name == "ПУМБ":
        return rates.pumb_bank()

    if name == "АЛЬФА-БАНК":
        return rates.alfa_bank()

    if name == "Mono":
        return rates.mono()

    if name == "Ощад Банк":
        return rates.oschad_bank()

def war_info():
    return RussianInvading().army_losses()


def cripta():
    return BinaceCoinRating().return_coin_list()
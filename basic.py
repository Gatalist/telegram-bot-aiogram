import asyncio
from xml.etree.ElementTree import indent
from binance import AsyncClient, Client

import random, requests, json, datetime
from bs4 import BeautifulSoup

from settings import USER_WEB_LIST, ZODIAK_DAY_LIST, ZODIAK_LIST, WEATHER_CITY_LIST


class Browser:
    def __init__(self):
        self.user_list = USER_WEB_LIST
        self.day_list = ZODIAK_DAY_LIST
        self.zodiak_list = ZODIAK_LIST
        self.citys = WEATHER_CITY_LIST

    def get_user_agent(self):    
        return random.choice(self.user_list)
 
    def parse_url(self, link):
        headers = {'User-Agent': self.get_user_agent()}
        response = requests.get(link, headers=headers)
        result = BeautifulSoup(response.text, 'html.parser')
        return result


# парсинг сайта гороскопа
class Horoscope(Browser):
    def __init__(self):
        super().__init__()
       
    def search(self, name, data):
        zodiak = self.zodiak_list.get(name)
        day = self.day_list.get(data)
        link = f'https://orakul.com/horoscope/astrologic/more/{zodiak}/{day}.html'
        soup = self.parse_url(link)
        print(link)
        try:
            res_date = soup.find('div', {"class":"sm-descr"}).text
            res_text = (soup.find('div', {"class":"horoBlock"}).text).strip()
            return f'{name}\n\n{res_date}\n\n{res_text}'

        except:
            return "Попробуйте еще раз"


# парсинг сайта погоды
class Weather(Browser):
    def __init__(self):
        super().__init__()
        
    def get_city(self, town):
        city = self.citys.get(town)
        print(city)
        link = f'https://weather.com/ru-RU/weather/today/l/{city}'
        parser = self.parse_url(link)
        
        table = parser.find_all('div', {"class":"ListItem--listItem--25ojW WeatherDetailsListItem--WeatherDetailsListItem--1CnRC"})
        # sun = f"{parser.find('div', {'class':'SunriseSunset--datesContainer--2cHyj'}).text}"
        sun = parser.find('div', {'class':'SunriseSunset--datesContainer--1a5tE'})
        sun_up_dn_ = sun.find_all('p', {'class':'SunriseSunset--dateValue--N2p5B'})

        update = f"Обновлено в - {parser.find('span', {'class':'CurrentConditions--timestamp--23dfw'}).text[17:23]}\n"
        sun_up_dn = f"Восход - {sun_up_dn_[0].text} 🌘  Заход - {sun_up_dn_[1].text} 🌒\n\n"
        status = f"{parser.find('div', {'class':'CurrentConditions--phraseValue--2Z18W'}).text}\n"
        grade = f"Температура - {parser.find('span', {'class':'CurrentConditions--tempValue--MHmYY'}).text} 🌡\n"
        airs = f"Качество воздуха - {parser.find('text', {'class':'DonutChart--innerValue--3_iFF'}).text}/100 💭\n"
        airs_text = f"{parser.find('span', {'class':'AirQualityText--severity--1smy9'}).text}\n"
        airs_speed = f"Ветер - {table[1].find('span', {'class':'Wind--windWrapper--3Ly7c undefined'}).text[14:]} 💨\n"
        humidity = f"Влажность - {table[2].find('div', {'class':'WeatherDetailsListItem--wxData--kK35q'}).text} 💧\n"
        pressure = f"Давление - {table[4].find('span', {'class':'Pressure--pressureWrapper--3SCLm undefined'}).text[10:]}"

        try:
            return update + sun_up_dn + status + grade + airs + airs_text + airs_speed + humidity + pressure

        except:
            return "Попробуйте еще раз"


# парсинг сайта курса валют
class ExchangeRates(Browser):
    def __init__(self):
        super().__init__()

    def alfa_bank(self):
        link = 'https://alfabank.ua/ru/currency-exchange'
        parser = self.parse_url(link)

        try:
            table = parser.find_all('h4', {"class":"exchange-rate-tabs__info-value"})
            usd = f"USD {table[0].text.strip()} / {table[1].text.strip()}\n"
            eur = f"EUR {table[2].text.strip()} / {table[3].text.strip()}\n"
        
            return usd + eur
        
        except:
            return "Не удалось обновить"


    def pumb_bank(self):
        link = 'https://www.pumb.ua'
        parser = self.parse_url(link)
        
        try:
            table = parser.find_all('div', {"class":"rates-block"})

            usd = f"USD {table[1].text.strip()} / {table[2].text.strip()}\n"
            eur = f"EUR {table[4].text.strip()} / {table[5].text.strip()}\n"
            gbp = f"GBP {table[7].text.strip()} / {table[8].text.strip()}\n"
            pln = f"PLN {table[10].text.strip()} / {table[11].text.strip()}\n"
        
            return usd + eur + gbp + pln

        except:
            return "Не удалось обновить"


    def mtb_bank(self):
        link = 'https://www.mtb.ua/currency/'
        parser = self.parse_url(link)

        rates = parser.find_all('span', {"class":"exchange-value_num"})

        try:
            usd = f"USD {rates[0].text.strip()} / {rates[3].text.strip()}\n"
            eur = f"EUR {rates[1].text.strip()} / {rates[4].text.strip()}\n"
            gbp = f"GBP {rates[2].text.strip()} / {rates[5].text.strip()}\n"
            return usd + eur + gbp

        except:
            return "Не удалось обновить"


    def pivden_bank(self):
        link = 'https://bank.com.ua'
        parser = self.parse_url(link)

        try:
            date = f"{parser.find('p', {'class':'uikit__p course-table__date'}).text.strip()}\n\n"
            table = parser.find_all('span', {"class":"course-table__rate"})
            usd = f"USD {table[0].text.strip()} / {table[1].text.strip()}\n"
            eur = f"EUR {table[3].text.strip()} / {table[4].text.strip()}"
            return date + usd + eur

        except:
            return "Не удалось обновить"


    def nbu_bank(self):
        link = 'https://minfin.com.ua/currency/nbu'
        parser = self.parse_url(link)

        table = parser.find_all('td', {"class":"sc-1x32wa2-8 tWvco"})
        date_rates = f"{parser.find('span', {'class':'tjc6dx-0 kfulYb'}).text}\n\n"
        
        try:
            eur = f"EUR {table[0].find('p', {'class':'sc-1x32wa2-9 glerpA'}).text}\n"
            pln = f"PLN {table[1].find('p', {'class':'sc-1x32wa2-9 glerpA'}).text}\n"
            rub = f"RUB {table[2].find('p', {'class':'sc-1x32wa2-9 glerpA'}).text}\n"
            usd = f"USD {table[3].find('p', {'class':'sc-1x32wa2-9 glerpA'}).text}\n"

            return date_rates + eur + pln + rub + usd

        except:
            return "Не удалось обновить"


    def mono(self):
        link = 'https://api.monobank.ua/bank/currency'
        # Request data from link as 'str'
        response = requests.get(link).text
        # convert 'str' to Json
        data = json.loads(response)
        print(data)
        result = ''

        for curency in data:
            if int(curency['currencyCodeA']) == 840 and int(curency['currencyCodeB']) == 980:
                date_time = datetime.datetime.fromtimestamp(curency['date'])
                date = f"{date_time.strftime('%Y-%m-%d')}\n\n"
                usd = f"USD {curency['rateBuy']} / {curency['rateSell']}\n"
                result += date
                result += usd
            if int(curency['currencyCodeA']) == 978 and int(curency['currencyCodeB']) == 980:
                eur = f"EUR {curency['rateBuy']} / {curency['rateSell']}"
                result += eur

        return result


    def oschad_bank(self):
        link = 'https://www.oschadbank.ua/currency-rate'

        parser = self.parse_url(link)

        try:
            date = f"{parser.find('time', {'class':'heading-block-currency-rate__date'}).text.strip()}\n\n"
            rates = parser.find_all('td', {"class":"heading-block-currency-rate__table-col"})

            usd = f"USD {rates[9].text} / {rates[10].text}\n"
            eur = f"EUR {rates[15].text} / {rates[16].text}\n"
            gbp = f"GBP {rates[21].text} / {rates[22].text}\n"
            chf = f"CHF {rates[27].text} / {rates[28].text}\n"
            pln = f"PLN {rates[39].text} / {rates[40].text}"

            return date + usd + eur + gbp + chf + pln
       
        except:
            return "Не удалось обновить"


class RussianInvading(Browser):
    def __init__(self):
        super().__init__()

    def army_losses(self):
        link = 'https://index.minfin.com.ua/russian-invading/casualties/'
        parser = self.parse_url(link)

        try:
            table = parser.find_all('li', {"class":"gold"})

            date = table[0].find('span', {"class":"black"}).text
            list_machinery = table[0].find('div', {"class":"casualties"}).find_all('li')

            result = f"данные на {date}\n\n"

            for name in list_machinery:
                result += f"{name.text}\n"

            return result
        
        except:
            return "Не удалось обновить"

# парсинг топ криптовалют
class BinaceCoinRating():
    api_key = "VpdmH9tiJR9rZg0ARYpvJeLroNevlle799CwuNw1xoRNcn1p8pvS7McNOA1rGge5"
    api_secret = "E4QHvFPqYoodjixyo4Y3z5TjUuFn084epU8IVHNHE7rVJLx2ejgEvpXsAvcVgBNy"

    dont_bay_monet = ['BNB', 'BTC', 'ETH', 'RUB', 'UAH', 'EUR', 'GBP', 'TRY']
    # bay_monet = ['BUSD', 'USDT']
    bay_monet = ['USDT']

    def main(self):
        client = Client(self.api_key, self.api_secret)

        respons = client.get_ticker() # Get 24hr Ticker

        list_top_monet = {}

        for valuta in respons:
            if float(valuta["priceChangePercent"]) > 10:
                for monet in self.bay_monet:
                    if valuta["symbol"].endswith(monet):
                        list_top_monet[valuta["symbol"]] = float(valuta["priceChangePercent"])
                        # print(valuta)

        sorted_top_monet = sorted(list_top_monet.items(), key=lambda x:x[1], reverse=True)

        return sorted_top_monet

    def return_coin_list(self):
        res = self.main()
        # print(res)
        retern_text = f'Рост за 24 часа\n\n'

        for key, val in res:
            retern_text += f"{key} - {val}% ⬆️\n"

        # print(retern_text)
        return retern_text
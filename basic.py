import random
import requests
from bs4 import BeautifulSoup


class Browser:
    def __init__(self):
        self.user_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
            "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",\
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",\
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36",\
            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1", 
            ]

    def get_user_agent(self):    
        return random.choice(self.user_list)
 
    def parse_url(self, link):
        headers = {'User-Agent': self.get_user_agent()}
        response = requests.get(link, headers=headers)
        result = BeautifulSoup(response.text, 'html.parser')
        return result


class Horoscope(Browser):
    def __init__(self):
        super().__init__()
        self.day_list = {'Сегодня':'today', 'Вчера':'yesterday', 'Завтра':'tomorrow'}
        
        self.zodiak_list = {'♈ Овен':'aries', '♉ Телец':'taurus', '♊ Близнецы':'gemini',\
                            '♋ Рак':'cancer', '♌ Лев':'lion', '♍ Дева':'virgo', '♎ Весы':'libra',\
                            '♏ Скорпион':'scorpio', '♐ Стрелец':'sagittarius', '♑ Козерог':'capricorn',\
                            '♒ Водолей':'aquarius', '♓ Рыбы':'pisces'}

    def search(self, name, data):
        zodiak = self.zodiak_list.get(name)
        day = self.day_list.get(data)
        link = f'https://orakul.com/horoscope/astrologic/more/{zodiak}/{day}.html'
        soup = self.parse_url(link)

        try:
            res_date = soup.find('div', {"class":"sm-descr"}).text
            res_text = (soup.find('div', {"class":"horoBlock"}).text).strip()
            return f'{name}\n\n{res_date}\n\n{res_text}'

        except:
            return "Попробуйте еще раз"


class Weather(Browser):
    def __init__(self):
        super().__init__()
        self.citys = {'Одесса': '772c48ef169ca33289f573cfc0575bdb4b8de5428afa579db4f58b6409da27a5',\
                    'Киев': 'd198c31dca17aa9ac8e4ff2e4dbdb48e4ca8c01f0fd1369998f0a09f53ef0b1d',\
                    'Винница': '2261b41a35498e667410cb84dfb95d455f977b64d2c02b673df410b7d9ec31ed',\
                    'Луцк': '9ed1b131ff328739fae15bf25e0a49f1d34501daf2aa869cb1d90a4abd5b46a5',\
                    'Днепр': '18c057565e6a77ab8db20297aa3d63a95385590d82162f1cba1058074294d53a',\
                    'Донецк': '09967a3efc295696927d2dfb04bfa3158dd01196d1224dd072bc6874666002c1',\
                    'Житомир': 'c9f6f901e18cf9ff8c430ac48c811a40d8b6a852c024fa9f447098901061c8e2',\
                    'Ужгород': 'd1a4c2342d5998ab318ea3d2347dde79f3c82ce82334001e2b2299d5011f6f6d',\
                    'Запорожье': 'ad98cd3144fd119b42c9e6e71e71ae4a2ce6aae7b08cdc369344b7af43ceafbf',\
                    'Ивано-Франковск': 'fa503af746f1329a6f6de60f9f47ac0de7be325e973166d23b294e110fc2695d',\
                    'Кропивницкий': '2edb6e1b6faca6055f57db917526878835b3de10b243e5ba36d0065e4b022a88',\
                    'Луганск': '9c6dc2ab71544e5057f8156d336ab820e4fa020779dbfd8a3513e2d906f044da',\
                    'Львов': '98ef35fcef7257c1313f4b13a5ccb58f5db8da0afe41bb717c6ba097579ffa32',\
                    'Николаев': '8f9785ab85b7e846496b5889c0ba9c69d957b375d97888615efbd81b30a8cc59',\
                    'Тернополь': '458e68cf9072ee1bfabbfb406893a31efa89128c2a3e9a7e36b0c9c5e3913c9d',\
                    'Полтава': '147ae21468642ff98df8dd8cea2733c8ef8620d5f44c39223151e5643a6353d9',\
                    'Ровно': 'dae372cfea50c952738d812ef95a0e595266ff85bb98f23ff15f034384dd48f9',\
                    'Сумы': 'fb088e6509df12e6779a23ea195905ed913e124eb920100cfed204a24f488983',\
                    'Харьков': 'a4611f0d16cabf84398cffee7963a6f7817abe09168b0c01cfdcbb209451e775',\
                    'Херсон': 'b90f3826b2bf3e7db49cc623550a4488fe0e6868624ad0cbeff656644488a883',\
                    'Хмельницкий': '721275a2e48c2ce13c360c2d74dd3067f31a03a7d91aec6cf4ed3e75a9fef747',\
                    'Черкассы': '8475cf6880ae9b5b9c88ae4b47a366e4e1c489327bb98a109e38461ad8e78972',\
                    'Чернигов': 'd5a591c0fea07a88bafe951d05212c82c562b62777e06492bf0a9d0598e7a180',\
                    'Черновцы': '6f54d7ce444ce6e8cbc601d44ea101f21e23f78caca2d78b4b772e9b68805f41',\
                    }

    def get_city(self, town):
        city = self.citys.get(town)
        link = f'https://weather.com/ru-RU/weather/today/l/{city}'
        parser = self.parse_url(link)
        
        try:
            update = parser.find('span', {"class":"CurrentConditions--timestamp--23dfw"}).text
            status = parser.find('div', {"class":"CurrentConditions--phraseValue--2Z18W"}).text
            grade = parser.find('span', {"class":"CurrentConditions--tempValue--3a50n"}).text
            airs = parser.find('text', {"class":"DonutChart--innerValue--2rO41"}).text
            airs_text = parser.find('span', {"class":"AirQualityText--severity--1fu5k"}).text
        
            pm_all = parser.find_all('p', {"class":"SunriseSunset--dateValue--N2p5B"})
            pm = []
            for pm_elem in pm_all:
                pm.append(pm_elem.text)

            table_wind = parser.find('span', {"class":"Wind--windWrapper--3aqXJ undefined"}).text
            
            index_wind = parser.find('span', {"data-testid":"PercentageValue"}).text

            return f"\n{update} \n\n {status} \n🌡 Температура  {grade} \n💭 Индекс качества воздуха  {airs} {airs_text} \n🌘 Восход - {pm[0]} \
                    \n🌒 Заход - {pm[1]} \n💨 Ветер - {table_wind[14:]}  \n💧 Влажность - {index_wind}"
        except:
            return "Попробуйте еще раз"


class ExchangeRates(Browser):
    def __init__(self):
        super().__init__()

    def alfa_bank(self):
        link = 'https://alfabank.ua/ru/currency-exchange'
        parser = self.parse_url(link)

        rates = parser.find_all('h4', {"class":"exchange-rate-tabs__info-value"})
        rates_list = []
        
        try:
            for rate in rates:
                rates_list.append((rate.text).strip())

            return f"USD {rates_list[0]} / {rates_list[1]}\nEUR {rates_list[2]} / {rates_list[3]}"
        except:
            return "Не удалось обновить"

    def oschad_bank(self):
        link = 'https://oschadbank.ua/currency-rate'
        parser = self.parse_url(link)
        try:
            rates = parser.find_all('td', {"class":"heading-block-currency-rate__table-col"})
            rates_list = []
            i = 0
            for rate in rates:
                if i == 9 or i == 10 or i == 15 or i == 16:
                    rates_list.append(rate.text)
                i += 1

            return f"USD {rates_list[0]} / {rates_list[1]}\nEUR {rates_list[2]} / {rates_list[3]}"
        except:
            return "Не удалось обновить"

    def mtb_bank(self):
        link = 'https://www.mtb.ua/'
        parser = self.parse_url(link)

        try:
            rates = parser.find_all('span', {"class":"exchange-value_num"})
            rates_list = []
            for rate in rates:
                rates_list.append((rate.text).strip())
            
            return f"USD {rates_list[0]} / {rates_list[4]}\nEUR {rates_list[1]} / {rates_list[5]}\nRUB {rates_list[2]} / {rates_list[6]}\
                \nGBP {rates_list[3]} / {rates_list[7]}"

        except:
            return "Не удалось обновить"

    def pumb_bank(self):
        link = 'https://www.pumb.ua'
        parser = self.parse_url(link)

        try:
            rates = parser.find_all('div', {"class":"rates-block"})
            rates_list = []
            for rate in rates:
                rates_list.append((rate.text).strip())
            
            return f"USD {rates_list[3]} / {rates_list[4]}\nEUR {rates_list[6]} / {rates_list[7]}\nRUB {rates_list[9]} / {rates_list[10]}\
                \nGBP {rates_list[12]} / {rates_list[13]}\nPLN {rates_list[15]} / {rates_list[16]}"

        except:
            return "Не удалось обновить"

    def pivden_bank(self):
        link = 'https://bank.com.ua'
        parser = self.parse_url(link)

        try:
            rates = parser.find_all('span', {"class":"course-table__rate"})
            rates_list = []
            for rate in rates:
                rates_list.append((rate.text).strip())

            return f"USD {rates_list[0]} / {rates_list[1]}\nEUR {rates_list[3]} / {rates_list[4]}\nRUB {rates_list[6]} / {rates_list[7]}"

        except:
            return "Не удалось обновить"


    def nbu_bank(self):
        link = 'https://minfin.com.ua/currency/nbu'
        parser = self.parse_url(link)

        try:
            rates = parser.find_all('td', {"class":"responsive-hide td-collapsed mfm-text-nowrap mfm-text-right"})
            rates_list = []
            i = 0
            for rate in rates:
                if i < 4:
                    elem = (rate.text).strip()
                    split_elem = elem.split('\n')
                    elem_view = split_elem[0]
                    rates_list.append(elem_view[:-4])
                i += 1
            print(rates_list)
            return f"USD {rates_list[0]}\nEUR {rates_list[1]}\nRUB {rates_list[2]}\nGBP {rates_list[3]}"

        except:
            return "Не удалось обновить"

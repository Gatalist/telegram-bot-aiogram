from aiogram.utils.callback_data import CallbackData

API_TOKEN = '1096XXXXXX:AAXXXXXXXXXXXXXXXXXXXXXXXXXXXXxpA'

banks = ["MTB Банк", "НБУ курс", "Південний", "ПУМБ", "АЛЬФА-БАНК", "Ощад Банк", "Mono"]

zodiak_callback = CallbackData('vote', 'name', 'select_date')

USER_WEB_LIST = [
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
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]


ZODIAK_DAY_LIST = {
    'Сегодня':'today', 
    'Вчера':'yesterday', 
    'Завтра':'tomorrow'
    }
        

ZODIAK_LIST = {
    '♈ Овен':'aries', '♉ Телец':'taurus', '♊ Близнецы':'gemini', '♋ Рак':'cancer',\
    '♍ Дева':'virgo', '♎ Весы':'libra', '♏ Скорпион':'scorpio', '♐ Стрелец':'sagittarius',\
    '♑ Козерог':'capricorn', '♒ Водолей':'aquarius', '♓ Рыбы':'pisces', '♌ Лев':'lion'
}

zodiak = [ '♈ Овен', '♉ Телец', '♊ Близнецы', '♋ Рак',
           '♍ Дева', '♎ Весы', '♏ Скорпион', '♐ Стрелец',
           '♑ Козерог', '♒ Водолей', '♓ Рыбы', '♌ Лев'
         ]

WEATHER_CITY_LIST = {
    'Одесса': '772c48ef169ca33289f573cfc0575bdb4b8de5428afa579db4f58b6409da27a5',\
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

city_list = [
    'Одесса',
    'Киев',
    'Винница',
    'Луцк',
    'Днепр',
    'Донецк',
    'Житомир',
    'Ужгород',
    'Запорожье',
    'Ивано-Франковск',
    'Кропивницкий',
    'Луганск',
    'Львов',
    'Николаев',
    'Тернополь',
    'Полтава',
    'Ровно',
    'Сумы',
    'Харьков',
    'Херсон',
    'Хмельницкий',
    'Черкассы',
    'Чернигов',
    'Черновцы',
]

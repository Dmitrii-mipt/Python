import time
import requests
from bs4 import BeautifulSoup


class Cryptocurrency:
    BTC_RUB = 'https://www.google.ru/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&newwindow=1&source=hp&ei=5DmDYMe3HZGyrgTimqawBg&iflsig=AINFCbYAAAAAYINH9AXCvP41bZ7UphGyOcVywK1XbTcD&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQgwEyCAgAELEDEIMBMgIIADIFCAAQsQMyCAgAELEDEIMBMgIIADICCAAyAggAMgIIADIICAAQsQMQgwE6CAgAEMcBEK8BOg0IABCxAxCDARBGEIICOgIILlDaAliVEGC5ImgAcAB4AIABWYgBxwOSAQE2mAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz'
    BCH_RUB = 'https://www.google.ru/search?q=bitcoin+cash&newwindow=1&source=hp&ei=2MOGYPyHAa-dlwTDnbCYCg&iflsig=AINFCbYAAAAAYIbR6J6D7WH_KECMoJdreo2wTgt8S0RU&oq=bitcoin+cash&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEEYQggIyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6CAgAELEDEIMBOgsILhCxAxDHARCjAjoRCAAQsQMQgwEQiwMQqAMQ0gM6BQguELEDOgUIABCxAzoOCAAQsQMQiwMQqAMQ0gM6CAguEMcBEKMCOhEIABCxAxCDARCLAxDSAxCoAzoICC4QsQMQgwE6AgguOg0IABCxAxCDARBGEIICUOoLWL8jYJ4naABwAHgAgAH4AYgB3BKSAQUwLjkuM5gBAKABAaoBB2d3cy13aXq4AQI&sclient=gws-wiz&ved=0ahUKEwj809vOhZzwAhWvzoUKHcMODKMQ4dUDCAc&uact=5'
    EOS_RUB = 'https://coinmarketcap.com/ru/currencies/eos/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    diff_btc = 100000
    diff_bch = 10000
    diff_eos = 100
    btc_price = 0
    bch_price = 0
    eos_price = 0

    def __init__(self):
        self.btc_price = float(self.get_btc_price())
        self.bch_price = float(self.get_bch_price())
        self.eos_price = float(self.get_eos_price())

    def get_btc_price(self):
        full_page = requests.get(self.BTC_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
        return (convert[0].text.replace('\xa0', '')).replace(',', '.')

    def get_bch_price(self):
        full_page = requests.get(self.BCH_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
        return (convert[0].text.replace('\xa0', '')).replace(',', '.')

    def get_eos_price(self):
        full_page = requests.get(self.EOS_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('div', {'class': 'priceValue___11gHJ'})
        return convert[0].text.replace(',', '.')[1::]

    def check_cryptocurrency(self):
        price_btc = float(self.get_btc_price())
        price_bch = float(self.get_bch_price())
        price_eos = float(self.get_eos_price())
        if price_btc >= self.btc_price + self.diff_btc:
            print('Bitcoin сильно вырос')
        elif price_btc <= self.btc_price - self.diff_btc:
            print('Bitcoin сильно упал')
        if price_bch >= self.bch_price + self.diff_bch:
            print('Bitcoin Cash сильно вырос')
        elif price_bch <= self.bch_price - self.diff_bch:
            print('Bitcoin Cash сильно упал')
        if price_eos >= self.eos_price + self.diff_eos:
            print('EOS сильно вырос')
        elif price_eos <= self.eos_price - self.diff_eos:
            print('EOS сильно упал')
        print('Сейчас: 1 Bitcoin = ' + str(self.btc_price) + ' руб')
        print('        1 Bitcoin Cash = ' + str(self.bch_price) + ' руб')
        print('        1 EOS = ' + str(self.eos_price) + ' руб')
        time.sleep(3600)
        self.check_cryptocurrency()

# -- coding: utf-8 --

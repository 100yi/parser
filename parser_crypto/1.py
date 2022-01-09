import requests
from bs4 import BeautifulSoup

class Crypto:
    def __init__(self, name):
        self.name = name

    html = requests.get('https://coinmarketcap.com/').text

    def get_value(self):
        cryptos = {
            'bitcoin': 0,
            'etherium': 1,
            'litecoin': 22,
        }

        soup = BeautifulSoup(self.html, 'lxml')
        table = soup.find('table', class_='cmc-table')
        table = table.find('tbody')
        trs = table.find_all('tr')
        num = cryptos.get(self.name)
        if num != None:
            tr = trs[num]
            tds = tr.find_all('td')
            try:
                crypto_name = tds[2].find('p').text
                price_in_usd = tds[3].text
                r = f"name - {crypto_name}, value - {price_in_usd}"
                return r
            except:
                r = tr.find_all('td')
                crypto_name = r[2].text
                price_in_usd = r[3].text
                r = f"name - {crypto_name}, value - {price_in_usd}"
                return r
        else:
            print('Have not this coin')

etherium = Crypto('etherium')
print(etherium.get_value())
bitcoin = Crypto('bitcoin')
print(bitcoin.get_value())
litecoin = Crypto('litecoin')
print(litecoin.get_value())

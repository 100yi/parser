# parser crypto
import requests
from bs4 import BeautifulSoup



class Crypto:
    cryptos = ['etherium', 'bitcoin', 'litecoin']
    @staticmethod
    def get_price_of_bitcoin():
        return


def get_html():
    url = 'https://coinmarketcap.com/'
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        return 'Error'

def get_crypto_rate(html, name):

    cryptos = {
        'bitcoin': 0,
        'etherium': 1,
        'litecoin': 22,
    }
    if name in cryptos:

        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('table', class_='cmc-table')
        table = table.find('tbody')
        trs = table.find_all('tr')
        tr = trs[cryptos.get(name)]
        tds = tr.find_all('td')
        try:
            crypto_name = tds[2].find('p').text
            price_in_usd = tds[3].text
            r = f"name - {crypto_name}, value - {price_in_usd}"
            print(r)
        except:
            r = tr.find_all('td')
            crypto_name = r[2].text
            price_in_usd = r[3].text
            r = f"name - {crypto_name}, value - {price_in_usd}"
            print(r)
    else:
        print('No crypto in bases')

def get_crypto_rate_all(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_='cmc-table')
    table = table.find('tbody')
    trs = table.find_all('tr')
    for i in range(0, 100):
        tr = trs[i]
        tds = tr.find_all('td')
        try:
            crypto_name = tds[2].find('p').text
            price_in_usd = tds[3].text
        except:
            r = tr.find_all('td')
            crypto_name = r[2].text
            price_in_usd = r[3].text
            print(crypto_name, price_in_usd)



def main():
    get_crypto_rate(get_html(), 'etherium')


if __name__ == '__main__':
    main()

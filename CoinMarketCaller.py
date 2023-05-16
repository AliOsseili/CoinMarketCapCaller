import requests
from requests import Session
import keys
from  pprint import pprint as pp

class CoinMarketCaller:
    def __init__(self,api_key):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': api_key,}
        self.session = Session()
        self.session.headers.update(self.headers)
        
    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        data = self.session.get(url)
        data = data.json()['data']
        return data
    def getPrice(self, symbol):
        url = self.apiurl + '/v2/cryptocurrency/quotes/latest'
        params = {'symbol': symbol}
        data = self.session.get(url,params=params)
        data = data.json()['data'][symbol][0]['quote']['USD']['price']
        return data

cmc = CoinMarketCaller(keys.API_KEY)

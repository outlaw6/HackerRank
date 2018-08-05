from bs4 import BeautifulSoup
import urllib.request
import requests, json
headers = {'X-CMC_PRO_API_KEY': 'd739a56a-0ca0-4be1-bd28-5a7321dcbc0f'}
r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?id=1', headers=headers)
am = r.json()

print(am['data'])
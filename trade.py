import requests
from config import *

BASE_URL = 'https://paper-api.alpaca.markets'

r = requests.get(BASE_URL, headers={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY})
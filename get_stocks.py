import requests, json
import alpaca_trade_api as tradeapi
import pandas as pd
from config import *


BASE_URL = "https://paper-api.alpaca.markets"
DATA_URL = "https://data.alpaca.markets"

api = tradeapi.REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL, api_version='v2')


#.get_barset(symbols, timeframe, limit, start=None, end=None, after=None, until=None)
#symbols --> String, or list of strings
#timeframe --> minute, 1Min, 5Min, 15Min, day,

#return: t: beginning time, o: open price, h: high price, l: low price, c: close price
#		 v: volume

time = pd.Timestamp(year=2020, month=5, day=8, hour=9)
barset = api.get_barset(symbols="AAPL", timeframe="minute", start=time, limit=20)



def to_pandas(barset):
	dataframe = {}
	for symbol in barset.keys():
		bars = barset[symbol]

		data = {"close": [bar.c for bar in bars],
				"high": [bar.h for bar in bars],
				"low": [bar.l for bar in bars],
				"open": [bar.o for bar in bars],
				"time": [bar.t for bar in bars],
				"volume": [bar.v for bar in bars]}
		dataframe[symbol] = pd.DataFrame(data)
	return dataframe


print (to_pandas(barset))
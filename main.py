import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style

import numpy as np
import datetime as dt
import urllib

style.use('fivethirtyeight')

def get_query(api_key, stock, interval='monthly'): 
  return 'https://www.alphavantage.co/query?function=TIME_SERIES_' + interval.upper() + '&symbol=MSFT&apikey=' + api_key + '&datatype=csv'

def get_stock_data(stock):
  api_key = open('../api-key-alpha-vantage.txt', 'r').read()
  stock_url = get_query(api_key, stock)
  source_code = urllib.request.urlopen(stock_url).read().decode()
  print(source_code)

get_stock_data('TSLA')
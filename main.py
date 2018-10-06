import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style

import numpy as np
import datetime as dt
import urllib

style.use('fivethirtyeight')

# Get formatted url for query
def get_query(api_key, stock, interval='monthly'): 
  return 'https://www.alphavantage.co/query?function=TIME_SERIES_' + interval.upper() + '&symbol=MSFT&apikey=' + api_key + '&datatype=csv'

def get_stock_data(stock):
  # Read api key and use in query
  api_key = open('../api-key-alpha-vantage.txt', 'r').read()
  stock_url = get_query(api_key, stock)
  source_code = urllib.request.urlopen(stock_url).read().decode()

  # Turn query into useable data
  stock_data = []
  split_source_code = source_code.split('\n')
  
  for line in split_source_code:
    split_line = line.split(',')
    if len(split_line) == 

get_stock_data('TSLA')
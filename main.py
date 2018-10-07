import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style

import numpy as np
import datetime as dt
import urllib

style.use('fivethirtyeight')

def convertToMPLDate(fmt, encoding='utf-8'):
  strconverter = mdates.strpdate2num(fmt)
  def converter(b):
    s = b.decode(encoding)
    return strconverter(s)
  return converter


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
  
  for line in split_source_code[1:]:
    split_line = line.split(',')
    if len(split_line) == 6:
      if 'timestamp' not in line:
        stock_data.append([split_line[0], float(split_line[1]), float(split_line[2])])

  fig = plt.figure()
  axis = plt.subplot2grid((1, 1), (0, 0))
  axis.grid(True)
  # axis.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
  # axis.xaxis.set_major_locator(mticker.MaxNLocator(10))

  # axis.plot(stock_data[0], stock_data[1]))

  stock_data = np.array(stock_data)

  print(stock_data.T[1])

get_stock_data('TSLA')
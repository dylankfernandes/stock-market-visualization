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
        stock_data.append([split_line[0], split_line[1], float(split_line[2])])

  # Declare the x and y list of variables
  stock_data = list(reversed(stock_data))
  stock_data = np.array(stock_data)
  x = stock_data.T[0]
  y = list(map(float, stock_data.T[1]))
  
  # Define the axis and figure
  fig = plt.figure()
  axis = plt.subplot2grid((1, 1), (0, 0))
  axis.plot_date(x, y, label='Stock Price')
  axis.xaxis.set_major_locator(mticker.MaxNLocator(10))
  axis.grid(True)

  # Rotate the date labels to better fit the graph
  for label in axis.xaxis.get_ticklabels():
    label.set_rotation(45)
  
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.title('Stock Data')
  plt.legend()
  plt.subplots_adjust(bottom=0.20, wspace=0.2, hspace=0)
  plt.show()

get_stock_data('TSLA')
#!/usr/bin/env python3
from v20 import V20Conn
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import re

image_dir = "images/matplot_out/"

def main():
  # Initiate API connection
  test = V20Conn()

  # Get series
  _s1 = test.GetHistory("2020-04-23","2020-04-24", "S5", 40)
  # Isolate candle data
  _candles = pd.DataFrame(_s1['candles'])

  # initialize empty dataframe
  _graph = pd.DataFrame()

  # Get closing prices for Ask and Bid
  _graph['closeAsk'] = _candles["closeAsk"]
  _graph['closeBid'] = _candles["closeBid"]

  # Get average of full Ask and Bid series
  _graph['closeAsk_avg'] = _candles["closeAsk"].mean()
  closeBid_avg = _candles["closeBid"].mean()

  # Get rolling/moving average for bid and ask, assign it to corresponding DataFrame
  _graph["_askRollingAvg_10"] = _candles["closeAsk"].rolling(window=10).mean()
  _graph["_bidRollingAvg_3"] = _candles["closeBid"].rolling(window=3).mean()

  _graph["_askRollingAvg_20"] = _candles["closeAsk"].rolling(window=20).mean()
  _graph["_bidRollingAvg_6"] = _candles["closeBid"].rolling(window=6).mean()


  # CLI output, only useful for debugging.
  # Will add to a debugging object later, is convenient for now
  print("\nGraph DataFrame:\n\n",_graph.tail(10))
  # print(
  #     '''
  #     Closing Ask Average:\t%s
  #     Closing Bid Average:\t%s
  #     '''
  #     % (closeAsk_avg,closeBid_avg)
  # )

  # MatPlotLib Graph
  plt.figure(figsize=[15,10])
  plt.grid(True)
  plt.plot(_graph['closeAsk'],label='Ask Close')
  plt.plot(_graph['_askRollingAvg_10'],label='SMA 10 Periods Ask')
  plt.plot(_graph['_askRollingAvg_20'],label='SMA 20 Periods Ask')
  plt.plot(_graph['closeAsk_avg'], label='Closing Ask AVG')
  plt.grid(True)
  # plt.ylim((1.000,2.000))
  plt.legend(loc=2)
  plt.show() # Needs GUI to display, otherwise please view file created below
  # Create filename and save file
  filename = image_dir + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") # Day-Month-Year_Hour-Min-Sec_(AM/PM)
  print("filename:\t\t%s" % (filename))
  plt.savefig(str(filename))


if __name__ == "__main__":
    main()
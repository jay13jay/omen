#!/usr/bin/env python3
from v20 import V20Conn
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import re

image_dir = "images/matplot_out/"

def main():
  test = V20Conn()
  _s1 = test.GetHistory("2020-04-23","2020-04-24", "S5", 1000)
  _len = len(_s1['candles'])
  _candles = pd.DataFrame(_s1['candles'])
  _graph = pd.DataFrame()

  # Set up graphing dataframe
  _graph['closeAsk'] = _candles["closeAsk"]
  _graph['closeBid'] = _candles["closeBid"]

  # Get average of full sequence
  closeAsk_avg = _candles["closeAsk"].mean()
  closeBid_avg = _candles["closeBid"].mean()

  # Get rolling/moving average for bid and ask
  _graph["_askRollingAvg_3"] = _candles["closeAsk"].rolling(window=20).mean()
  _graph["_bidRollingAvg_3"] = _candles["closeBid"].rolling(window=3).mean()

  _graph["_askRollingAvg_6"] = _candles["closeAsk"].rolling(window=30).mean()
  _graph["_bidRollingAvg_6"] = _candles["closeBid"].rolling(window=6).mean()


  print("\nGraph DataFrame:\n\n",_graph.tail(10))
  print(
      '''
      Closing Ask Average:\t%s
      Closing Bid Average:\t%s
      '''
      % (closeAsk_avg,closeBid_avg)
  )

  plt.figure(figsize=[15,10])
  plt.grid(True)
  plt.plot(_graph['closeAsk'],label='Ask Close')
  plt.plot(_graph['_askRollingAvg_3'],label='SMA 3 Periods Ask')
  plt.plot(_graph['_askRollingAvg_6'],label='SMA 6 Periods Ask')
  plt.legend(loc=2)
  # plt.show()

  # Create filename
  # print('date first:\t',datetime.now())
  # rightnow = str(datetime.now()).replace(" ", "_")
  # print('date before regex:\t',rightnow)
  # rightnow =re.sub(r"\.[0-9]*", "", rightnow)
  # print('date after regex:\t',rightnow)

  filename = image_dir + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")

  # filename = str(rightnow+'.png')
  print("filename:\t",filename)
  plt.savefig(str(filename))


if __name__ == "__main__":
    main()
#!/usr/bin/env python

import v20, configparser, oandapy
import pandas as pd


class V20Conn():
  def __init__(self):
    # Read config file
    config = configparser.ConfigParser()
    self.config = config
    self.config.read('oanda.cfg')

    try:
      self.account_id = config['OANDA']['account_id']
    except:
      exit("account_id not present in config file.\nPlease double check your configuration and try again")
    try:
      self.access_token = config['OANDA']['access_token']
    except:
      exit("access_token not present in config file.\nPlease double check your configuration and try again")
    try:
      self.hostname = config['OANDA']['hostname']
    except:
      self.hostname = "api-fxpractice.oanda.com"
    try:
      self.port = config['OANDA']['port']
    except:
      self.port = 443
    try:
      self.instrument = config['OANDA']['instrument']
    except:
      self.instrument = "EUR_USD"
    try:
      self.units = config['OANDA']['units']
    except:
      self.units = 1000
    try:
      self.environment = config['OANDA']['environment']
    except:
      self.environment = "practice"

    # Create the API context based on the provided arguments
    self.api = oandapy.API(environment=self.environment, access_token=self.access_token)

    return(None)

  def PrintConfig(self):
    print(
      '''
      Account ID:\t%s
      Hostname:\t\t%s
      Port:\t\t%s
      Instrument:\t%s
      Units:\t\t%s
      ''' % (self.account_id, self.hostname, self.port, self.instrument, self.units)
    )
    
  def GetHistory(self, _from, _to, granularity):
    _ret = self.api.get_history(
      instrument=self.instrument,
      units = self.units,
      granularity= granularity,
      # start=_from,
      # end=_to,
      count=2
    )
    return(_ret)
    


test = V20Conn()
# test.PrintConfig()
_s1 = test.GetHistory("2020-04-23","2020-04-24", "S5")
print(_s1)
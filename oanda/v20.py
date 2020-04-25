#!/usr/bin/env python

import v20, configparser


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
      self.instrument = "EUR/USD"
    try:
      self.units = config['OANDA']['units']
    except:
      self.units = 1000

    # Create the API context based on the provided arguments
    self.api_conn = v20.Context(
        self.hostname,
        self.port,
        token=self.access_token
    )

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
    
    


test = V20Conn()

test.PrintConfig()

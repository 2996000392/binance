def market_short(symbol, quantity,flag):
  url = 'https://fapi.binance.com/fapi/v1/order'
  timestamp = int(round(time.time() * 1000))
  query_string = 'timestamp=%s&symbol=%s&side=SELL&type=MARKET&quantity=%s' % (str(timestamp), symbol, str(quantity))
  signature = hashing(query_string)
  params = {
      'timestamp': timestamp,
      'signature': signature,
      'symbol': symbol,
      'side': 'SELL',
      'type': 'MARKET',
      'quantity': quantity,
  }
  r = requests.post(url=url, headers=headers, params=params).json()  
  print('开仓' + symbol, time.strftime("%Y-%m-%d %H:%M:%S"), '㊦㊦㊦㊦㊦', r, "\n")
  
 

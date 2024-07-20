import requests
import hashlib
import hmac
import time

api_key = '1zd8WOkPmkD9z7JYrya4gwh9qOldE3a5O2FJSBzaC2APBXT1XCrFBIXkxorxqqMH'
secret_key = 'j4wNZmLK0W1Cz7ShKEaVxfGB5JzdKnlfWmehj8tApyAoJFE4CSHNRoYpiceePRYZ'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'X-MBX-APIKEY': api_key
}

def hashing(query_string):
    return hmac.new(secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
	
def market_short(symbol, quantity): #市价开空
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
    
    
market_short('BBUSDT',15)		

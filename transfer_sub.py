import requests
import time
import hashlib
import hmac
from urllib.parse import urlencode


api_key = 'xxxxxxxxxxxxxxxxxxx’
secret_key = 'xxxxxxxxxxxxxxxxxxxx’

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'X-MBX-APIKEY': api_key
}

def hashing(query_string):
    return hmac.new(secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest() 


def transfer_sub(fromEmail,toEmail):
    url = 'https://api.binance.com/sapi/v1/sub-account/universalTransfer'
    timestamp = int(round(time.time() * 1000))   
    query_string = 'timestamp=%s&fromEmail=%s&toEmail=%s&fromAccountType=SPOT&toAccountType=SPOT&asset=USDT&amount=7' % (str(timestamp),str(fromEmail),str(toEmail))
    params = 
    {
        'fromEmail':fromEmail,
        'toEmail': toEmail,
        'fromAccounType':'SPOT',
        'toAccountType':'SPOT',
        'asset':'USDT',
        'amount': 0,
        'timestamp':timestamp,
        'signature': signature
    }
    params = urlencode(params, True).replace("%40", "@")
    rsponse = requests.post(url=url, headers=headers, params=params)

transfer_sub('xxx@qq.com', 'jflaj@qq.com')



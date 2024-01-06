from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json
from dotenv import load_dotenv
import os

load_dotenv()
apikey = os.getenv('apikey')
secretkey = os.getenv('secretkey')

client = Client(apikey,secretkey)
# get market depth
depth = client.get_order_book(symbol='BNBBTC')
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)

def price_btcusdt():
    info_cripto = client.get_avg_price(symbol='BTCUSDT')
    price = float(info_cripto["price"])
    return f'{price:.2f}'

if __name__ == '__main__':
    print(price_btcusdt())
    print(client.get_avg_price(symbol='BTCUSDT'))
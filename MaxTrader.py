import utils
import time
import binance_utils
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from binance.websockets import BinanceSocketManager
import traceback

binance = binance_utils.get_binance_account()
binance_coins = binance_utils.get_binance_buyable_coins(binance)


def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

bm = BinanceSocketManager(binance, user_timeout=60)
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
# then start the socket manager
bm.start()

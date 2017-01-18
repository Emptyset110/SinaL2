# -*- coding: utf-8 -*-
from SinaL2.SinaL2 import SinaL2
import threading
import time
import SinaL2.util as util

trading_date = util.get_trading_date()

def on_recv_data(message):
    print(util.ws_parse(message=message, to_dict=True, trading_date=trading_date))


def start_sina_l2():
    sina_l2 = SinaL2(symbols=["sz000001","sh600221"], on_recv_data=on_recv_data, query=["quotation","transaction","orders"])
    sina_l2.start()

t = threading.Thread(target=start_sina_l2)
t.setDaemon(True)
t.start()

while True:
    time.sleep(10)

# -*- coding: utf-8 -*-
from SinaL2 import SinaL2


def on_recv_data(message):
    print(message)

sina_l2 = SinaL2(symbols=["sz000001"], on_recv_data=on_recv_data)
sina_l2.start()

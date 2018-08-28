#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import threading
import time

def hello():
    print("現在のスレッドの数: " + str(threading.activeCount()))
    print("[%s] helohelo!!" % threading.currentThread().getName())
    print(time.time())
    t=threading.Timer(0.5,hello)
    t.start()

if __name__=='__main__':
    t_init=time.time()
    t=threading.Thread(target=hello)
    t.start()
    while(True):
        try:
            print("baba")
            time.sleep(3)
        except KeyboardInterrupt:
            break

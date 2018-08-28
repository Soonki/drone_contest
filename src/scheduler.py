#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, threading

class Scheduler():

    def __init__(self,function,step_time):
        self.stop_event = threading.Event() #停止させるかのフラグ
        self.inc_event = threading.Event()  #刻み幅を増やすかのフラグ
        self.step_time=step_time
        self.function=function
        self.count=0
        #スレッドの作成と開始
        self.thread = threading.Thread(target = self.run)
        self.thread.start()
        

    def run(self):
        self.count+=1
        self.function()

        if not self.stop_event.is_set():
            self.thread=threading.Timer(self.step_time,self.run)
            self.thread.start()

    def stop(self):
        """スレッドを停止させる"""
        self.stop_event.set()
        self.thread.join()    #スレッドが停止するのを待つ

    def inc(self):
        self.inc_event.set()

if __name__ == '__main__':

    def hello():
        print("hello")
    
    def bab():
        print("Babu")

    h = Scheduler(hello,0.5)      #スレッドの開始
    b = Scheduler(bab,2)
    time.sleep(6)
    h.stop()        #スレッドの停止
    b.stop()
    print "finish"
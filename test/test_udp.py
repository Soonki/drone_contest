#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import numpy as np
import cv2
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ソケットオブジェクト作成

s.bind(("192.168.13.2", 10001))    # サーバー側PCのipと使用するポート

print("接続待機中")  

s.listen(1)                     # 接続要求を待機

soc, addr = s.accept()          # 要求が来るまでブロック

print(str(addr)+"と接続完了")  

cam = cv2.VideoCapture(0)#カメラオブジェクト作成
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 48)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 32)


while (True):
  
  try:

    flag,img = cam.read()       #カメラから画像データを受け取る

    img = np.array(img)

    img = img.tostring()        #numpy行列からバイトデータに変換
  
    soc.send(img)              # ソケットにデータを送信
    #print(img.shape())
    time.sleep(0.1)            #フリーズするなら#を外す。

  except KeyboardInterrupt:
    break

cam.release()                  #カメラオブジェクト破棄
s.shutdown()
s.close()

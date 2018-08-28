#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 48)
i=0
N=100

print("START")
while(True):
    i=i+1
    # フレームをキャプチャする
    
    ret, frame = cap.read()
    
    path = "fig/photo" + str(i) + ".jpg"
    print(path)
    cv2.imwrite(path,frame)

    if i==N:
        break
    time.sleep(0.5)

# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()

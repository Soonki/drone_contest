#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import time

i=0
detect_circle=[]

# カメラが有効な間ループ
while(True):
    i=i+1
    # 画像を読み取る
    file = "fig/photo" + str(i) + ".jpg"
    frame = cv2.imread(file)
    

    # RGB（赤青緑）からHSV(色味、鮮やかさ、明るさ)に変換する
    cam_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 特定の色だけのマスクを作る
    cam_hsv = cv2.inRange(cam_hsv, (0,200,100), (5,255,255))
    #cv2.imshow('preview', cam_hsv)
    # オリジナルの画像をコピーし、マスクされている部分を0にする（黒くする）
    cam_color = frame.copy()
    cam_color[cam_hsv==0] = 0

    # ゴマ粒ノイズを消すためのマスクを用意する
    element = np.ones((5,5)).astype(np.uint8)

    # ゴマ粒ノイズを消す（？）ために膨張収縮させる
    cam_hsv = cv2.erode(cam_hsv, element)
    cam_hsv = cv2.dilate(cam_hsv, element)

    # ノイズを消し、しかもオリジナルの画像にマスク処理をして不要な部分をつぶした画像に対して、円の検出処理をする
    # この時、「外接円」を探す
    points = np.dstack(np.where(cam_hsv>0)).astype(np.float32)
    center, radius = cv2.minEnclosingCircle(points)
    if radius > 150 or radius < 20:
        center = (0.0,0.0)
        radius = 0.0
    cv2.circle(frame, (int(center[1]), int(center[0])), int(radius), (255,0,0), thickness=3)
    cv2.circle(cam_hsv, (int(center[1]), int(center[0])), int(radius), (255,0,0), thickness=3)
    #cv2.imshow('preview', cam_hsv)
    result = "result/photo" + str(i) + ".jpg"
    cv2.imwrite(result,cam_hsv)
    print(center,radius)

    if radius > 10:
        detect_circle.append(i)
    #time.sleep(3)

    if i == 100:
        break

print(detect_circle)
print(len(detect_circle))
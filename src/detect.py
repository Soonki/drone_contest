#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

class detect():
    def __init__(self):
        self.element=np.ones((5,5)).astype(np.uint8)
        self.RED_CIRCLE=0
        self.BLUE_SQUARE=0
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 48)

    def detect_red_circle(self,gray_img,debag=False):
        # 特定の色だけのマスクを作る
        gray_img = cv2.inRange(gray_img,(0,50,50), (7,255,255))
        #cv2.imshow('preview', cam_hsv)


        # ゴマ粒ノイズを消す（？）ために膨張収縮させる
        gray_img = cv2.erode(gray_img, self.element)
        gray_img = cv2.dilate(gray_img, self.element)

        # ノイズを消し、しかもオリジナルの画像にマスク処理をして不要な部分をつぶした画像に対して、円の検出処理をする
        # この時、「外接円」を探す
        points = np.dstack(np.where(gray_img>0)).astype(np.float32)
        center, radius = cv2.minEnclosingCircle(points)
        if radius > 10 or radius < 0:
            center = (0.0,0.0)
            radius = 0.0

        #if debag == True
            #cv2.circle(, (int(center[1]), int(center[0])), int(radius), (255,0,0), thickness=3)
            

        return not radius == 0.0

    def detect_blue_square(self,gray_img,debag=False):
        # 特定の色だけのマスクを作る
        gray_img = cv2.inRange(gray_img, (80,50,0), (160,255,255))
        #cv2.imshow('preview', cam_hsv)

        # ゴマ粒ノイズを消す（？）ために膨張収縮させる
        gray_img = cv2.erode(gray_img, self.element)
        gray_img = cv2.dilate(gray_img, self.element)

        # ノイズを消し、しかもオリジナルの画像にマスク処理をして不要な部分をつぶした画像に対して、円の検出処理をする
        points = np.dstack(np.where(gray_img>0)).astype(np.float32)
        rect = cv2.minAreaRect(points)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        _, contours, hierarchy = cv2.findContours(gray_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        max_area=0
        max_area_countor=-1

        for j in range(len(contours)):
            area = cv2.contourArea(contours[j])
            if max_area<area and area > 50:
                max_area=area
                max_area_countor=j

        #print(max_area_countor)
        #print(contours)
        #if not max_area_countor == -1:
            #cv2.drawContours(cam_hsv, contours, max_area_countor, (0,255,0), 3)
            #cv2.drawContours(frame, contours, max_area_countor, (0,255,0), 3)
        return not max_area_countor == -1

    def detect_all(self):
        #t=time.time()
        _,img=self.cam.read()
        #t_get=time.time()-t
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#0.05sくらい
        #t_gray=time.time()-t
        
        if self.detect_red_circle(img):#0.13sくらい
            self.RED_CIRCLE=1
        else:
            self.RED_CIRCLE=0
        #t_red=time.time()-t
        
        if self.detect_blue_square(img):
            self.BLUE_SQUARE=1
        else:
            self.BLUE_SQUARE=0
        #t_blue=time.time()-t
        #print(t_get,t_gray,t_red,t_blue)
        return self.RED_CIRCLE,self.BLUE_SQUARE

    def detect_and_blink(self):
        self.detect_all()
        
        return self.RED_CIRCLE,self.BLUE_SQUARE



if __name__=='__main__':
    import time
    det=detect()
    while(det.cam.isOpened()):
        t=time.time()
        #cam_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #print(det.detect_red_circle(cam_hsv))
        #print(det.detect_blue_square(cam_hsv))
        try:
            R,B=det.detect_all()
            print("R:",R,"B",B,"time",time.time()-t)
        except KeyboardInterrupt:
            det.cam.release()
            print("Complite")
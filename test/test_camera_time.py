#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import time

cam = cv2.VideoCapture(0)

while(cam.isOpened()):
    t=time.time()
    time.sleep(1)
    print(time.time()-t)
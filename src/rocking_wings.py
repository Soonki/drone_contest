#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import time

class rocking_wings():
    def __init__(self,vehicle):
        self.count=0
        self.motion_data=np.genfromtxt("../motion/motion_data.csv",delimiter=",")
        #print(self.motion_data)
        self.vehicle=vehicle
        self.motion_step=len(self.motion_data)
        #self.motion_read_data=np.empty([1,5])
        self.motion_read_data=np.array([[0,1,2,3,4]])

    def run(self):#スレッドで回す想定
        self.count+=1
        if self.count < self.motion_step:
            self.vehicle.channels.overrides = {'1':self.motion_data[self.count][1], '2':self.motion_data[self.count][2],'3':self.motion_data[self.count][3],'4':self.motion_data[self.count][4]}
        else:
            self.clear()

    def read_motion(self):
        data=np.array([[time.time(),self.vehicle.channels['1'],self.vehicle.channels['2'],self.vehicle.channels['3'],self.vehicle.channels['4']]])
        self.motion_read_data=np.append(self.motion_read_data,data,axis=0)

    def save_motion(self):
        np.savetxt("../motion/motion_data.csv", self.motion_read_data, delimiter=",")

    def clear(self):
        self.vehicle.channels.overrides = {}

if __name__=='__main__':
    pass
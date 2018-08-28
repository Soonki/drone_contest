#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mode import mode
from dronekit import connect, VehicleMode
from servo import servo
import time
from detect import detect
from scheduler import Scheduler
from rocking_wings import rocking_wings

class copter():

    def setup(self):
        print("Connecting")
        self.vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600,rate=2,use_native=True,heartbeat_timeout=-1)        
        self.MODE=mode(self.vehicle)
        self.CAMERA=detect()

        self.ROCK=rocking_wings(self.vehicle)
        self.count=0
        self.flag=0
        self.RED_CIRCLE=0
        self.BLUE_SQUARE=0
        self.mode_thread=Scheduler(self.MODE.updateMode,0.5)
        print("Complite Initial Setup")

    def loop(self):
        t=time.time()        

        if self.MODE.CAMERA==True and self.MODE.ROCKING_WINGS==False:
            #detect circle and square
            self.RED_CIRCLE,self.BLUE_SQUARE=self.CAMERA.detect_all()
            #処理時間がかかる

        if self.MODE.CAMERA==False and self.MODE.ROCKING_WINGS==True:
            self.rock_thread=Scheduler(self.ROCK.read_motion,0.5)

        if self.MODE.RCSAFETY == 1:
            #diarm and throttle off
            self.count=self.count+1
    
        if self.count>5:
            self.flag=True

        if time.time()-t<0.5:
            time.sleep(0.5-time.time()+t)
        #print(time.time()-t)
    
        return self.flag

    def end(self):
        print("End Start")
        self.mode_thread.stop()
        self.rock_thread.stop()
        self.vehicle.close()
        self.CAMERA.cam.release()
        print("Completed")


if __name__=="__main__":

    COPTER=copter()
    COPTER.setup()
    while(COPTER.CAMERA.cam.isOpened()):
        try:
            t=time.time()
            flag=COPTER.loop()

            #print("SERVO:%d" % COPTER.MODE.SERVO,time.time()-t)
            #print("R:",COPTER.RED_CIRCLE,"B:",COPTER.BLUE_SQUARE)
            if flag == True:
                break

        except KeyboardInterrupt:
            break

    COPTER.end()
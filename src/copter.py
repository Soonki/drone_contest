#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mode import mode
from dronekit import connect, VehicleMode
from servo import servo
import time
from detect import detect
from scheduler import Scheduler
from rocking_wings import rocking_wings
from led import led

class copter():

    def setup(self):
        print("Connecting")
        self.vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600,rate=2,use_native=True,heartbeat_timeout=-1)        
        self.MODE=mode(self.vehicle)
        self.CAMERA=detect()
        self.led=led()
        self.ROCK=rocking_wings(self.vehicle)
        self.count=0
        self.flag=0
        self.flag_count=25
        self.dt=0.1
        self.RED_CIRCLE=0
        self.BLUE_SQUARE=0
        self.mode_thread=Scheduler(self.MODE.updateMode,0.5)
        self.rock_thread=Scheduler(self.ROCK.run,0.25)
        self.mode_thread.start()
        print("Complite Initial Setup")
        self.led.flash_second(3)

    def setup_read_motion(self):
        print("Connecting")
        self.vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600,rate=2,use_native=True,heartbeat_timeout=-1)        
        self.MODE=mode(self.vehicle)
        self.CAMERA=detect()
        self.led=led()
        self.ROCK=rocking_wings(self.vehicle)
        self.count=0
        self.flag=0
        self.flag_count=25
        self.dt=0.1
        self.RED_CIRCLE=0
        self.BLUE_SQUARE=0
        self.mode_thread=Scheduler(self.MODE.updateMode,0.5)
        self.rock_thread=Scheduler(self.ROCK.read_motion,0.25)
        self.mode_thread.start()
        print("Complite Initial Setup")
        self.led.flash_second(3)

    def loop(self):
        t=time.time()        

        if self.MODE.CAMERA==True and self.MODE.ROCKING_WINGS==False:
            #detect circle and square
            self.RED_CIRCLE,self.BLUE_SQUARE=self.CAMERA.detect_all()
            self.led.blink(self.RED_CIRCLE,self.BLUE_SQUARE)

        if self.MODE.CAMERA==False and self.MODE.ROCKING_WINGS==False:
            self.led.off_both()

        if self.MODE.CAMERA==False and self.MODE.ROCKING_WINGS==True and self.rock_thread.state==0:
            print("Rocking Wings!!")
            self.led.blink_all()
            self.rock_thread.start()

        if self.MODE.ROCKING_WINGS==False and self.rock_thread.state==1:
            print("End Rocking Wings")
            self.led.off_both()
            self.rock_thread.stop()
            self.ROCK.clear()
            self.rock_thread=Scheduler(self.ROCK.run,0.25)

        if self.MODE.RCSAFETY == 1:
            #self.vehicle.channels.overrides['3']=950
            self.vehicle.armed=False
            self.count=self.count+1
    
        if self.count>self.flag_count:
            self.flag=True
        #print(time.time()-t)
        if time.time()-t<self.dt:
            time.sleep(self.dt-time.time()+t)
        
        return self.flag

    def end(self):
        print("End Start")
        self.led.flash_second(3)
        self.mode_thread.stop()
        if self.rock_thread.state==1:
            self.rock_thread.stop()
            
        if len(self.ROCK.motion_read_data) > 3:
            self.ROCK.save_motion()
        self.vehicle.close()
        self.CAMERA.cam.release()
        print("Completed")

    def loop_read_motion(self):
        t=time.time()        

        if self.MODE.CAMERA==True and self.MODE.ROCKING_WINGS==False:
            #detect circle and square
            self.RED_CIRCLE,self.BLUE_SQUARE=self.CAMERA.detect_all()
            self.led.blink(self.RED_CIRCLE,self.BLUE_SQUARE)

        if self.MODE.CAMERA==False and self.MODE.ROCKING_WINGS==False:
            self.led.off_both()

        if self.MODE.CAMERA==False and self.MODE.ROCKING_WINGS==True and self.rock_thread.state==0:
            print("Rocking Wings!!")
            self.led.blink_all()
            self.rock_thread.start()

        if self.MODE.ROCKING_WINGS==False and self.rock_thread.state==1:
            print("End Rocking Wings")
            self.led.off_both()
            self.rock_thread.stop()
            self.rock_thread=Scheduler(self.ROCK.read_motion,0.25)

        if self.MODE.RCSAFETY == 1:
            #self.vehicle.channels.overrides['3']=950
            self.vehicle.armed=False
            self.count=self.count+1
    
        if self.count>self.flag_count:
            self.flag=True
        #print(time.time()-t)
        if time.time()-t<self.dt:
            time.sleep(self.dt-time.time()+t)
        
        return self.flag

    def end(self):
        print("End Start")
        self.led.flash_second(3)
        self.mode_thread.stop()
        if self.rock_thread.state==1:
            self.rock_thread.stop()
            
        if len(self.ROCK.motion_read_data) > 3:
            self.ROCK.save_motion()
        self.vehicle.close()
        self.CAMERA.cam.release()
        print("Completed")


if __name__=="__main__":

    COPTER=copter()
    COPTER.setup()
    while(True):#COPTER.CAMERA.cam.isOpened()):
        try:
            t=time.time()
            flag=COPTER.loop()

            #print("SERVO:%d" % COPTER.MODE.SERVO,time.time()-t)
            #print("R:",COPTER.RED_CIRCLE,"B:",COPTER.BLUE_SQUARE)
            if flag == True:
                print("Safety")
                break

        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break

    COPTER.end()
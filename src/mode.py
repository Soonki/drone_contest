#!/usr/bin/python
# -*- coding: utf-8 -*-
#モードクラス　サーボも込で

#from servo import servo
import time

class mode():
    def __init__(self,vehicle):
        self.SERVO=0
        self.SERVO_MODE=0
        self.ROCKING_WINGS=0
        self.CAMERA=0
        self.RCSAFETY=0
        self.vehicle=vehicle
        #self.motor=servo()

    def updateMode(self):
        if int(self.vehicle.channels['6']) > 1800:
            self.SERVO = 1
        else:
            self.SERVO = 0
        #self.motor.updateMotor(self.SERVO)
        #self.SERVO_MODE=abs(self.motor.flag)

        if int(self.vehicle.channels['7']) > 1800 and self.vehicle.mode.name=='ALT_HOLD':
            self.ROCKING_WINGS = True
            self.CAMERA = False
        elif int(self.vehicle.channels['7']) < 1400:
            self.ROCKING_WINGS = False
            self.CAMERA = True
        else:
            self.ROCKING_WINGS = False
            self.CAMERA = False

        if int(self.vehicle.channels['8']) > 1800:
            self.RCSAFETY = True
        else:
            self.RCSAFETY = False

    def getMode(self):
        return self.SERVO,self.ROCKING_WINGS,self.CAMERA,self.RCSAFETY

if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    import time
    
    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    mode=mode(vehicle)

    while(True):
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()

        if int(vehicle.channels['3']) > 1800:
            break

        print("SERVO:%d" % SERVO)
        print("ROCKING WINGS:%d" % ROCKING_WINGS)
        print("CAMERA:%d" % CAMERA)
        print("RCSAFETY:%d" % RCSAFETY)
        time.sleep(0.5)
    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")



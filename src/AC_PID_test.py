#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mode import mode
from dronekit import connect, VehicleMode
import time

class AC_PID():
    def __init__(self,vehicle):
        #ゲイン設定、スラスト初期値
        self.Kp=700
        self.Kd=50
        self.Ki=50
        self.thrust_input=1100
        #PIDcontroller初期値
        self.e_pre=0#1ループ前の偏差
        self.e=0
        self.e_dif=0
        self.e_int=0
        #制御器周波数
        self.dt=0.01

        self.vehicle=vehicle


    def controller(self,target_altitude,mode):
        print("AUTO_TAKEOFF start!")
        while True:
            current_altitude=getaltitude()

            #auto_takeoff 終了判定
            if current_altitude>=target_altitude:
                print("Reach target altitude")
                Set_thrust(0)
                break

            mode.updateMode()
            SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()
            print("Now_mode: ",vehicle.mode)

            #セーフティ機能
            if SERVO == 0:
                print("Saftey mode 自動離陸中断します")
                break

            PID_process(current_altitude,target_altitude)

            Set_thrust(self.thrust_input)


    def getaltitude(self):
        current_altitude = self.vehicle.rangefinder.distance
        print("current_altitude: ",current_altitude)
        return current_altitude

    def PID_process(self,current_altitude,target_altitude):
        self.e=target_altitude-current_altitude
        self.edif=(self.e-self.e_pre)/self.dt
        self.e_int=self.e_int+self.e*dt

        self.thrust_input=1100+self.Kp*self.e+self.Kd*self.edif0+self.Ki*self.e_int

        self.e_pre=self.e

        #Thrust_Saturation
        if self.thrust_input>=1900:
            self.thrust_input=1900

    def Set_thrust(self,override):
        self.vehicle.channels.overrides = {'4':override}


if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    from mode import mode
    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    mode=mode(vehicle)
    #PIDControllerオブジェクト作成
    AC=AC_PID(vehicle)
    #目標高度
    target_altitude=0.6
    takeoff_count=0


    while(True):
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()
        print("======================================")
        print(vehicle.mode)
        print("======================================")

        #自動離陸モード
        if SERVO==1　and takeoff_count==0:
            controller(target_altitude,mode)
            print("Auto take-off sequence ends")
            takeoff_count=1

        if  RCSAFETY == 1:
            break


        print(":::::::::::::::::::::::::::::::::::::::::")
        print("SERVO:%d" % SERVO)
        print("ROCKING WINGS:%d" % ROCKING_WINGS)
        print("CAMERA:%d" % CAMERA)
        print("RCSAFETY:%d" % RCSAFETY)
        print(":::::::::::::::::::::::::::::::::::::::::")
        time.sleep(0.5)

        #自動着陸？
        # print("Setting LAND mode...")
        # vehicle.mode = VehicleMode("LAND")
        # time.sleep(1)
    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")

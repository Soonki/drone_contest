#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mode import mode
from dronekit import connect, VehicleMode
import time

class AC_PID():
    def __init__(self,vehicle):
        #ゲイン設定、スラスト初期値
        self.Kp=350
        self.Kd=50
        self.Ki=50
        self.thrust_input=1100
        #PIDcontroller初期値
        self.e_pre=0#1ループ前の偏差
        self.e=0
        self.e_dif=0
        self.e_int=0
        #制御器周波数
        self.dt=0.1

        self.vehicle=vehicle
        self.takeoff_count=0
        #Thrustの値設定
        self.Thrust_Saturation=1750
        self.Thrust_Standard=1500


    def controller(self,target_altitude,mode):
        print("AUTO_TAKEOFF start!")
        print("---------------------------------")
        self.e_pre=target_altitude
        while True:
            start_time=time.time()
            current_altitude=self.getaltitude()

            #auto_takeoff 終了判定
            if current_altitude>=target_altitude:
                print("Reach target altitude")
                self.clear()
                self.e_int=0
                break

            mode.updateMode()
            SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()
            print("SERVO: ",SERVO)
            print(vehicle.mode.name)

            #セーフティ機能
            if SERVO == 0 or RCSAFETY == 1:
                print("Saftey mode 自動離陸中断します")
                self.clear()
                self.e_int=0
                break

            self.PID_process(current_altitude,target_altitude)

            self.Set_thrust()

            required_time=time.time()-start_time
            time_A=self.dt-required_time
            time.sleep(time_A)


    def getaltitude(self):
        current_altitude = self.vehicle.rangefinder.distance
        print("current_altitude: ",current_altitude)
        return current_altitude

    def PID_process(self,current_altitude,target_altitude):
        self.e=target_altitude-current_altitude
        self.e_dif=(self.e-self.e_pre)/self.dt
        self.e_int=self.e_int+self.e*self.dt

        self.thrust_input=self.Thrust_Standard+self.Kp*self.e+self.Kd*self.e_dif+self.Ki*self.e_int

        self.e_pre=self.e

        print("Control_input_pre: ",self.thrust_input)

        #Thrust_Saturation
        if self.thrust_input>=self.Thrust_Saturation:
            self.thrust_input=self.Thrust_Saturation

    def Set_thrust(self):
        self.vehicle.channels.overrides = {'3':self.thrust_input}
        print("override: ",self.thrust_input)

    def clear(self):
        self.vehicle.channels.overrides = {}


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


    while(True):
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()
        print("======================================")
        print(vehicle.mode)
        print("======================================")

        #自動離陸モード
        if SERVO==1 and AC.takeoff_count==0:
            AC.controller(target_altitude,mode)
            print("Auto take-off sequence ends")
            AC.takeoff_count=1
            print("---------------------------------")

        #モードフラグの初期化処理
        if SERVO==0 and AC.takeoff_count==1 and AC.getaltitude()<=0.2:
            AC.takeoff_count=0
            print("再度、自動離陸可能")

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

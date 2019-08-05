from  dronekit import connect, VehicleMode
import time
print("start")
vehicle = connect('/dev/ttyS0' , wait_ready = True, baud =  57600)
print("start2")

while True:
    if int(vehicle.channels['6']) > 1800:
        vehicle.channels.overrides = {"3" : 500,"1" : 500}
        print("failsafe!!")
        time.sleep(0.1)
        break
    else:
        vehicle.channels.overrides = {}
        print("Normal")
        time.sleep(0.1)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from dronekit import connect,VehicleMode
def get_altitude(vehicle):
    current_altitude = vehicle.location.global_relative_frame.alt
    current_altitude2 = vehicle.rangefinder.distance
    print("location_func: ",current_altitude,"  rangefinder: ",current_altitude2)





if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode, Rangefinder
    from mode import mode
    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    mode=mode(vehicle)

    while(True):
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()

        get_altitude(vehicle)

        if  RCSAFETY == 1:
            break

        print("SERVO:%d" % SERVO)
        print("ROCKING WINGS:%d" % ROCKING_WINGS)
        print("CAMERA:%d" % CAMERA)
        print("RCSAFETY:%d" % RCSAFETY)
        time.sleep(0.5)
    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")

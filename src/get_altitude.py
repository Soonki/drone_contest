#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
def get_altitude():
    current_altitude = vevehicle.location.global_relative_frame.alt
    print(current_altitude)





if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    from mode import mode
    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    mode=mode(vehicle)

    while(True):
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()

        get_altitude()

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

#!/usr/bin/python
# -*- coding: utf-8 -*-

def update_mode(vehicle):
    if int(vehicle.channels['6']) > 1800:
        SERVO = True
    else:
        SERVO = False

    if int(vehicle.channels['7']) > 1800:
        ROCKING_WINGS = True
        CAMERA = False
    elif int(vehicle.channels['7']) < 1400:
        ROCKING_WINGS = False
        CAMERA = True
    else:
        ROCKING_WINGS = False
        CAMERA = False

    if int(vehicle.channels['8']) > 1800:
        RCSAFETY = True
    else:
        RCSAFETY = False
    return SERVO,ROCKING_WINGS,CAMERA,RCSAFETY


if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    import time
    
    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    while(True):
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = update_mode(vehicle)

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


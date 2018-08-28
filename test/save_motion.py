#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    import time,csv
    
    frq=4
    dt=1/frq
    RC_Y=[]
    RC_P=[]
    RC_T=[]
    RC_R=[]
    time_stamp=[]
    all_data=[]

    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    mode=mode(vehicle)

    while(True):
        t=time.time()
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()

        if RCSAFETY == True:
            break

        if ROCKING_WINGS == 1:
            t_save=time.time()
            while(True):
                mode.updateMode()
                SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()
                
                RC_Y.append(int(vehicle.channels['1'])
                RC_P.append(int(vehicle.channels['2'])
                RC_T.append(int(vehicle.channels['3'])
                RC_R.append(int(vehicle.channels['4'])
                time_stamp.append(time.time()-t_save)

                if ROCKING_WINGS == 0:
                    break
            all_data.append(time_stamp)
            all_data.append(RC_Y)
            all_data.append(RC_P)
            all_data.append(RC_T)
            all_data.append(RC_R)
            with open('data.csv','w') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerows(all_data)

        #print("SERVO:%d" % SERVO)
        #print("ROCKING WINGS:%d" % ROCKING_WINGS)
        #print("CAMERA:%d" % CAMERA)
        #print("RCSAFETY:%d" % RCSAFETY)
        time.sleep(dt-time.time()+t)
    # Close vehicle object before exiting script
    vehicle.close()
    print("Completed")
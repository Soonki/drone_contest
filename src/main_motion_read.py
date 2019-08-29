from copter import copter

COPTER=copter()
COPTER.setup_read_motion()
while(COPTER.CAMERA.cam.isOpened()):
    try:
        #t=time.time()
        flag=COPTER.loop_read_motion()
        COPTER.output_mode()
        #print("SERVO:%d" % COPTER.MODE.SERVO,time.time()-t)
        #print("R:",COPTER.RED_CIRCLE,"B:",COPTER.BLUE_SQUARE)
        if flag == True:
            print("Safety")
            break

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break

COPTER.end()

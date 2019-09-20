
#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import shlex

class stream():
    def __init__(self):
        self.camera_flag=0
    def start(self):
        if self.camera_flag==0:
            #cmd = "sh start_server.sh"
            cmd= "/usr/local/bin/mjpg_streamer -i \"input_raspicam.so -x 640 -y 480 -fps 3 -q 10\" -o \"output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www\" -b"
            #https://qiita.com/ego/items/3d23cda713f29f0dd141
            cmd = shlex.split(cmd)
            ret = subprocess.check_output(cmd)
            print(ret)
            print("streaming start!")
            self.camera_flag=1
    def end(self):
        if self.camera_flag==1:
            #cmd="sh end_server.sh"
            cmd2="pidof mjpg_streamer"
            cmd2 = shlex.split(cmd2)
            try:
                ret2 = subprocess.check_output(cmd2)
                print(ret2)            
                cmd="kill -9 "+ret2
                cmd = shlex.split(cmd)
                ret = subprocess.check_output(cmd)
                print(ret)
                print("end streaming")
            except:
                print("streaming start error!")
            self.camera_flag=0


if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    from mode import mode
    import commands
    import time
    import pigpio
    import threading
    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    mode=mode(vehicle)
    stream=stream()

    while(True):
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()

        if CAMERA == True and stream.camera_flag==0:
            stream.start()
        if CAMERA==False and stream.camera_flag==1:
            stream.end()
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


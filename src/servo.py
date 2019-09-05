
import pigpio
import time

class servo():
    def __init__(self):
        self.gpio_pin0 = 18
        self.pi = pigpio.pi()
        self.pi.set_mode(self.gpio_pin0, pigpio.OUTPUT)
        self.motorstate = True
        self.pos_min=113600
        self.pos_up1=70000
        self.pos_up2=26100
        self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_min)
        self.flag=0

    def changeMotorstate(self):
        if self.motorstate:
            output=self.pos_max
        else:
            output=self.pos_min
        self.pi.hardware_PWM(self.gpio_pin0, 50, output)
        self.motorstate=not self.motorstate

    #def upMotor_1(self):
    #    self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_up1)
    #def upMotor_2(self):
    #    self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_up2)
    #def downMotor(self):
    #    self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_min)
    def updateMotor(self,SERVO):
        if SERVO != 0 and self.flag == 0: #release mini chicken
            self.flag=SERVO
        if SERVO - self.flag != 0 and abs(self.flag)-1 == 0: #release big chicken
            self.flag=2
        if SERVO != 0 and self.flag == 2:
            self.flag=3
        if SERVO == 0 and self.flag > 2:
            self.flag=0
        
        if self.flag == 0:
            output=self.pos_min
        elif abs(self.flag)-1 == 0:
            output=self.pos_up1
        else:
            output=self.pos_up2
        self.pi.hardware_PWM(self.gpio_pin0, 50,output)


if __name__ == '__main__':
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    from mode import mode
    # Connect to the Vehicle.
    print("Connecting")
    vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

    mode=mode(vehicle)
    servo=servo()

    while(True):
        mode.updateMode()
        SERVO,ROCKING_WINGS,CAMERA,RCSAFETY = mode.getMode()

        servo.updateMotor(SERVO)

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


import pigpio
import time

class servo():
    def __init__(self):
        self.gpio_pin0 = 18
        self.pi = pigpio.pi()
        self.pi.set_mode(self.gpio_pin0, pigpio.OUTPUT)
        self.motorstate = True
        self.pos_min=26100
        self.pos_up1=113600
        self.pos_up2=70000
        self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_min)

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
        if SERVO == 2 :
            output=self.pos_up2
            #self.upMotor_2()
        elif SERVO == 1 :
            output=self.pos_up1
            #self.upMotor_1()
        else:
            output=self.pos_min
            #self.downMotor()
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

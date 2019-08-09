
import pigpio
import time

class servo():
    def __init__(self):
        self.gpio_pin0 = 18
        self.pi = pigpio.pi()
        self.pi.set_mode(self.gpio_pin0, pigpio.OUTPUT)
        self.motorstate = True
    	self.pos_min=22000
    	self.pos_max=78000
        self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_max)

    def changeMotorstate(self):
        if self.motorstate:
            output=self.pos_max
        else:
            output=self.pos_min
        self.pi.hardware_PWM(self.gpio_pin0, 50, output)
        self.motorstate=not self.motorstate

    def upMotor(self):
        self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_max)

    def downMotor(self):
        self.pi.hardware_PWM(self.gpio_pin0, 50, self.pos_min)

    def updateMotor(self,flag):
        if flag == 0:
            self.upMotor()
        else:
            self.downMotor()


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

        if SERVO == 0:
            servo.upMotor()
        else:
            servo.downMotor()

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

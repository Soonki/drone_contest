import pigpio
import time

class led():
    def __init__(self):
        self.pi=pigpio.pi()
        self.pin_red=12
        self.pin_blue=6
        self.pi.set_mode(self.pin_red,pigpio.OUTPUT)
        self.pi.set_mode(self.pin_blue,pigpio.OUTPUT)

    def blink_only_red(self):
        self.pi.write(self.pin_red,1)
        self.pi.write(self.pin_blue,0)

    def blink_only_blue(self):
        self.pi.write(self.pin_red,0)
        self.pi.write(self.pin_blue,1)

    def blink_all(self):
        self.pi.write(self.pin_red,1)
        self.pi.write(self.pin_blue,1)

    def off_both(self):
        self.pi.write(self.pin_red,0)
        self.pi.write(self.pin_blue,0)

    def blink(self,red,blue):
        self.pi.write(self.pin_red,red)
        self.pi.write(self.pin_blue,blue)

    def flash_second(self,second):
        i=0
        while(i < second):
            self.blink_all()
            time.sleep(0.2)
            self.off_both()
            time.sleep(0.2)
            i+=0.4

if __name__=="__main__":
    
    led=led()
    led.flash_second(3)
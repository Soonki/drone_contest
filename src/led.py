import pigpio

class led():
    def __init__(self):
        self.pi=pigpio.pi()
        self.pin_red=23
        self.pin_blue=24
        self.pi.set_mode(self.pin_red,pigpio.OUTPUT)
        self.pi.set_mode(self.pin_blue,pigpio.OUTPUT)

    def blink_only_red(self):
        self.pi.write(self.pin_red,1)
        self.pi.write(self.pin_blue,0)

    def blink_only_blue(self):
        self.pi.write(self.pin_red,0)
        self.pi.write(self.pin_blue,1)

    def blink(self,red,blue):
        self.pi.write(self.pin_red,red)
        self.pi.write(self.pin_blue,blue)
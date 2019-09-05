#!/usr/bin/python
# -*- coding: utf-8 -*-

import pigpio
import time

gpio_pin0 = 18

pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)

pwm1=113600
pwm2= 70000
pwm3= 26100
#サーボPWM幅
#上限：110000強
#下限： 27000弱

# GPIO18: 2Hz、duty比0.5
#pi.hardware_PWM(gpio_pin0, 50, 100000)
pi.hardware_PWM(gpio_pin0, 50,pwm1)
print(pwm1)
time.sleep(2)
pi.hardware_PWM(gpio_pin0, 50,pwm2)
print(pwm2)
time.sleep(2)
pi.hardware_PWM(gpio_pin0, 50, pwm3)
print(pwm3)
time.sleep(2)
pi.hardware_PWM(gpio_pin0, 50, pwm1)
print(pwm1)
pi.stop()

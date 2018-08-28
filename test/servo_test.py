#!/usr/bin/python
# -*- coding: utf-8 -*-

import pigpio
import time

gpio_pin0 = 18

pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)

# GPIO18: 2Hz、duty比0.5
pi.hardware_PWM(gpio_pin0, 50, 100000)
time.sleep(1)
pi.hardware_PWM(gpio_pin0, 50, 42000)

pi.stop()

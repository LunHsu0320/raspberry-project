#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme.

GPIO.setup(17, GPIO.OUT)  # set GPIO 17 as output for white led
GPIO.setup(27, GPIO.OUT)  # set GPIO 27 as output for red led
GPIO.setup(22, GPIO.OUT)  # set GPIO 22 as output for red led

blue = GPIO.PWM(17, 100)
green = GPIO.PWM(27, 100)
red = GPIO.PWM(22, 255)
i = 0


try:
    while True:
        if i < 100:
            i += 10
        else:
            i = 10
        blue.start(i)  # start blue led
        sleep(0.05)
        blue.stop()
        sleep(0.05)
        print(i)
        green.start(i)  # start green led
        sleep(0.05)
        green.stop()
        sleep(0.05)
        print(i)
        red.start(i)  # start red led
        sleep(0.05)
        red.stop()
        sleep(0.05)
        print(i)
except KeyboardInterrupt:
    blue.stop()
    red.stop()
    green.stop()
    GPIO.cleanup()  # clean up GPIO on CTRL+C exit
    print("END")

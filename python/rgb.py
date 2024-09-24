#!/usr/bin/python3

from gpiozero import RGBLED
from time import sleep

my_led = RGBLED(13, 19, 26, active_high=True)# change to False for common Anode RGBLEDs RGB and Cyan Mangenta Yellow

my_led.color = (1, 0, 0)
print("Red...")
sleep(2)

my_led.color = (0, 1, 0)
print("Green...")
sleep(2)

my_led.color = (0, 0, 1)
print("Blue...")
sleep(2)

my_led.color = (1, 1, 1)
print("White...")
sleep(2)

#!/usr/bin/python3

from gpiozero import RGBLED
from time import sleep

my_led = RGBLED(13, 19, 26)

my_led.color = (1, 1, 1)
print("White...")
sleep(200)

import RPi.GPIO as GPIO
import json


GPIO.setmode(GPIO.Board)
inputs = [1, 2, 3, 4, 5]
outputs = [6, 7, 8, 9, 10]


for input in inputs:
    setup_pins(input, "input")


def setup_pins(pin, setup):
    if setup == "input":
        setup = GPIO.IN
    if setup == "output":
        setup = GPIO.OUT
    GPIP.setup(pin, setup)

    print("setup input pin")

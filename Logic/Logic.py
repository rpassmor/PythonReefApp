import RPi.GPIO as GPIO


def one_input_one_output(input_pin, output_pin):
    on_off_switch = GPIO.input(input_pin)
    if on_off_switch:
        GPIO.output(output_pin, GPIO.HIGH)
    else:
        GPIO.output(output_pin, GPIO.LOW)
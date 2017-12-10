#Import libraries
from gpiozero import *
from time import sleep
import random

#Configure GPIO pins
led_blue = LED(16)
led_green = LED(20)
led_red = LED(12)
led_yellow = LED(7)
led_rgb = RGBLED(red=14, green=15, blue=18)
button_blue = Button(23)
button_green = Button(24)
button_red = Button(25)
button_yellow = Button(8)
buzzer = Buzzer(21)

#Create lists
correct_sequence = []
input_sequence = []

#Button detection function
def button_detect():
    if button_blue.is_pressed:
        input_sequence.append("blue")
        sleep(0.5)
    elif button_green.is_pressed:
        input_sequence.append("green")
        sleep(0.5)
    elif button_red.is_pressed:
        input_sequence.append("red")
        sleep(0.5)
    elif button_yellow.is_pressed:
        input_sequence.append("yellow")
        sleep(0.5)

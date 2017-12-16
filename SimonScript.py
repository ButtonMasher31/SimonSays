#Import libraries
from gpiozero import *
from time import sleep
import random

#Configure GPIO pins
led_blue = LED(16)
led_green = LED(20)
led_red = LED(12)
led_yellow = LED(7)
sequence_yellow = LED(15)
sequence_green = LED(14)
sequence_blue = LED(18)
sequence_red = LED(26)
button_blue = Button(23)
button_green = Button(24)
button_red = Button(25)
button_yellow = Button(8)
buzzer = Buzzer(21)

#Create lists and variables
correct_sequence = []
input_sequence = []
availible_colours = ["blue", "green", "red", "yellow"]
max_sequence_length = random.randint(1, 10)
sequence_length = 0

#Button detection function
def button_detect(colours):
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

#Sequence generator function
def sequence_generate():
    sequence_length =+ 1
    for i in range(sequence_length):
        colours.append(availible_colours[random.randint(1, 4)])
    for i in range(sequence_length):
        if colours[i] == "green":

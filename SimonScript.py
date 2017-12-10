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

#Create lists and variables
correct_sequence = []
input_sequence = []
availible_colours = ["blue", "green", "red", "yellow"]
colours = []
max_sequence_length = random.randint(1, 10)
sequence_length = 0
blue = 0, 0, 1
red = 1, 0, 0
green = 0, 1, 0
yellow = 0.25, 0.3, 0.25

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
def sequence_generator(colours):
    sequence_length =+ 1
    for i in range(0, sequence_length):
        correct_sequence.append(availible_colours[random.randint(0, 3)])
    for i in range(0, sequence_length):
        if correct_sequence[i] == "blue":
            colours.append(blue)
        elif correct_sequence[i] == "red":
            colours.append(red)
        elif correct_sequence[i] == "green":
            colours.append(green)
        elif correct_sequence[i] == "yellow":
            colours.append(yellow)
        print(correct_sequence)
    if sequence_length
    del colours
sequence_generator(colours)
sequence_generator(colours)
sequence_generator(colours)
sequence_generator(colours)
sequence_generator(colours)
sequence_generator(colours)

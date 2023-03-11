from microbit import *
import random
image_list = [Image.HAPPY,Image.SAD,Image.HEART,Image.HEART_SMALL]

while True:
    if button_a.was_pressed():
        display.show(random.choice(image_list))

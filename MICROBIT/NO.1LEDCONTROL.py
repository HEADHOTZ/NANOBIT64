# Write your code here :-)
from microbit import *

X = 2
Y = 2

while True:
    if button_a.is_pressed():
        while button_a.is_pressed():
            sleep(10)
        display.clear()
        X -= 1
        if X < 0:
            X = 4

    if button_b.is_pressed():
        while button_b.is_pressed():
            sleep(10)
        display.clear()
        X += 1
        if X > 4:
            X = 0

    if not pin12.read_digital():
        while not pin12.read_digital():
            sleep(10)
        display.clear()
        Y -= 1
        if Y < 0:
            Y = 4

    if not pin16.read_digital():
        while not pin16.read_digital():
            sleep(10)
        display.clear()
        Y += 1
        if Y > 4:
            Y = 0

    display.set_pixel(X , Y, 9)

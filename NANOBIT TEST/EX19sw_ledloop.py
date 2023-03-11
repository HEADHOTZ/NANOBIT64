from microbit import *
x = 0
y = 0

while True:
    if button_a.was_pressed():
        for y in range(0, 5):
            for x in range(0, 5):
                display.set_pixel(x, y, 9)
                sleep(200)

        for y in range(4, -1, -1):
            for x in range(4, -1, -1):
                display.set_pixel(x, y, 0)
                sleep(200)

    if button_b.was_pressed():
        for y in range(0, 5):
            for x in range(0, 5):
                display.set_pixel(x, y, 9)
                sleep(200)

        for y in range(0, 5):
            for x in range(0, 5):
                display.set_pixel(x, y, 0)
                sleep(200)

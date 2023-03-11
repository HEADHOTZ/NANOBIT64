from microbit import *

bImage_1 = Image("99999:"
                 "96669:"
                 "96369:"
                 "96669:"
                 "99999:")

while True:
    if button_a.is_pressed() and not button_b.is_pressed():
        display.show(Image.DIAMOND)
        sleep(500)
        display.clear()
        display.show(Image.DIAMOND_SMALL)
        sleep(500)
        display.clear()
        display.set_pixel(2, 2, 9)
        sleep(500)
        display.clear()

    if button_b.is_pressed() and not button_a.is_pressed():
        display.show(bImage_1)
        sleep(500)
    """ LED ขยับติดไปตามแกน Y ก่อน
    if button_a.is_pressed() and button_b.is_pressed():
        for X in range(0, 5):
            for Y in range(0, 5):
                display.set_pixel(X, Y, 9)
                sleep(200)

        for X in range(0, 5):
            for Y in range(0, 5):
                display.set_pixel(X, Y, 0)
                sleep(200)
"""
    if button_a.is_pressed() and button_b.is_pressed(): // ติดไปตามแกน X
        for Y in range(0, 5):
            for X in range(0, 5): // ทำในลูปในก่อนแล้วตามด้วยลูปนอก
                display.set_pixel(X, Y, 9)
                sleep(200)

        for Y in range(0, 5):
            for X in range(0, 5):
                display.set_pixel(X, Y, 0)
                sleep(200)

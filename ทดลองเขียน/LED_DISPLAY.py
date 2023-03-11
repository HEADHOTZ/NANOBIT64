from microbit import *
mode = 0
while True:
    if button_a.was_pressed():
        display.clear()
        mode += 1
        if mode > 4:
            mode = 1
    if button_b.was_pressed():
        display.clear()
        mode -= 1
        if mode < 1:
            mode = 4
    if mode == 1:
        display.show(Image.HEART)
    elif mode == 2:
        display.show(Image.HEART_SMALL)
    elif mode == 3:
        display.show(Image.DIAMOND)
    elif mode == 4:
        display.show(Image.DIAMOND_SMALL)

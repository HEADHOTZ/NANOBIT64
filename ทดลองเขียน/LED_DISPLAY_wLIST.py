from microbit import *
mode = -1
image_list = [Image.HEART,Image.HEART_SMALL,Image.DIAMOND,Image.DIAMOND_SMALL]
while 1:
    if button_a.was_pressed():
        mode += 1
        if mode > 3:
            mode = 0
        print(mode)
        display.show(image_list[mode])
    if button_b.was_pressed():
        mode -= 1
        if mode < 0:
            mode = 3
        print(mode)
        display.show(image_list[mode])

from iled4 import *
import gc
import music
gc.collect()
Min = 0
Sec = 30

f = iled4()
# decimals on
"""
for i in range(4):
    f.set_decimal(i)
    f.update_display()
    sleep(1000)
# decimals off
for i in range(4):
    f.set_decimal(i, False)
    f.update_display()
    sleep(1000)
"""
# print something
# f.print(1234)
# f.print(Min + Sec)
while True:
    if not pin12.read_digital():
        while not pin12.read_digital():
            sleep(10)
        Sec += 1
        if Sec > 59:
            Sec = 0
            Min += 1
    if not pin13.read_digital():
        while not pin13.read_digital():
            sleep(10)
        Min += 1
        if Min > 59:
            Min = 0
    if button_a.is_pressed() and button_b.is_pressed():
        while Sec > 0 or Min > 0:
            Sec -= 1
            if Sec < 0 and Min > 0:
                Sec = 59
                Min -= 1
            f.print((Min * 100) + Sec)
            f.update_display()
            sleep(100)
        if Sec == 0 and Min == 0:
            display.show(Image.HAPPY)
            music.play(music.DADADADUM)
            break
    f.print((Min * 100) + Sec)
    f.update_display()

# clear the display
# f.clear()
# sleep(1000)
# blink the colon
"""
for i in range(4):
    f.set_colon()
    f.update_display()
    sleep(500)
    f.set_colon(False)
    f.update_display()
    sleep(500)

# do some counting
for i in range(10000):
    f.print(i)
    f.update_display()
    sleep(50)"""

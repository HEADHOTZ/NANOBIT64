from microbit import *
import neopixel
np = neopixel.NeoPixel(pin14, 12)
enter = pin8
esc = pin12
num0 = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
num11 = 0
# num = [num1,num2]
while 1:
    y = int(pin2.read_analog() * 11 / 1023)
    if y == 0:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num0 += 1
        if num0 > 2:
            num0 = 0
        # if num[y]
        if num0 == 0:
            r0 = 255
            g0 = 0
            b0 = 0
        elif num0 == 1:
            r0 = 0
            g0 = 255
            b0 = 0
        elif num0 == 2:
            r0 = 0
            g0 = 0
            b0 = 255
        np[0] = (r0, g0, b0)
    if y == 1:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num1 += 1
            if num1 > 2:
                num1 = 0
        if num1 == 0:
            r1 = 255
            g1 = 0
            b1 = 0
        elif num1 == 1:
            r1 = 0
            g1 = 255
            b1 = 0
        elif num1 == 2:
            r1 = 0
            g1 = 0
            b1 = 255
        np[1] = (r1, g1, b1)
    if y == 2:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num2 += 1
            if num2 > 2:
                num2 = 0
        if num2 == 0:
            r2 = 255
            g2 = 0
            b2 = 0
        elif num2 == 1:
            r2 = 0
            g2 = 255
            b2 = 0
        elif num2 == 2:
            r2 = 0
            g2 = 0
            b2 = 255
        np[2] = (r2, g2, b2)
    if y == 3:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num3 += 1
            if num3 > 2:
                num3 = 0
        if num3 == 0:
            r3 = 255
            g3 = 0
            b3 = 0
        elif num3 == 1:
            r3 = 0
            g3 = 255
            b3 = 0
        elif num3 == 2:
            r3 = 0
            g3 = 0
            b3 = 255
        np[3] = (r3, g3, b3)
    if y == 4:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num4 += 1
            if num4 > 2:
                num4 = 0
        if num4 == 0:
            r4 = 255
            g4 = 0
            b4 = 0
        elif num4 == 1:
            r4 = 0
            g4 = 255
            b4 = 0
        elif num4 == 2:
            r4 = 0
            g4 = 0
            b4 = 255
        np[4] = (r4, g4, b4)
    if y == 5:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num5 += 1
            if num5 > 2:
                num5 = 0
        if num5 == 0:
            r5 = 255
            g5 = 0
            b5 = 0
        elif num5 == 1:
            r5 = 0
            g5 = 255
            b5 = 0
        elif num5 == 2:
            r5 = 0
            g5 = 0
            b5 = 255
        np[5] = (r5, g5, b5)
    if y == 6:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num6 += 1
            if num6 > 2:
                num6 = 0
        if num6 == 0:
            r6 = 255
            g6 = 0
            b6 = 0
        elif num6 == 1:
            r6 = 0
            g6 = 255
            b6 = 0
        elif num6 == 2:
            r6 = 0
            g6 = 0
            b6 = 255
        np[6] = (r6, g6, b6)
    if y == 7:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num7 += 1
            if num7 > 2:
                num7 = 0
        if num7 == 0:
            r7 = 255
            g7 = 0
            b7 = 0
        elif num7 == 1:
            r7 = 0
            g7 = 255
            b7 = 0
        elif num7 == 2:
            r7 = 0
            g7 = 0
            b7 = 255
        np[7] = (r7, g7, b7)
    if y == 8:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num8 += 1
            if num8 > 2:
                num8 = 0
        if num8 == 0:
            r8 = 255
            g8 = 0
            b8 = 0
        elif num8 == 1:
            r8 = 0
            g8 = 255
            b8 = 0
        elif num8 == 2:
            r8 = 0
            g8 = 0
            b8 = 255
        np[8] = (r8, g8, b8)
    if y == 9:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num9 += 1
            if num9 > 2:
                num9 = 0
        if num9 == 0:
            r9 = 255
            g9 = 0
            b9 = 0
        elif num9 == 1:
            r9 = 0
            g9 = 255
            b9 = 0
        elif num9 == 2:
            r9 = 0
            g9 = 0
            b9 = 255
        np[9] = (r9, g9, b9)
    if y == 10:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num10 += 1
            if num10 > 2:
                num10 = 0
        if num10 == 0:
            r10 = 255
            g10 = 0
            b10 = 0
        elif num10 == 1:
            r10 = 0
            g10 = 255
            b10 = 0
        elif num10 == 2:
            r10 = 0
            g10 = 0
            b10 = 255
        np[10] = (r10, g10, b10)
    if y == 11:
        if not enter.read_digital():
            while not enter.read_digital():
                sleep(10)
            num11 += 1
            if num11 > 2:
                num11 = 0
        if num11 == 0:
            r11 = 255
            g11 = 0
            b11 = 0
        elif num11 == 1:
            r11 = 0
            g11 = 255
            b11 = 0
        elif num11 == 2:
            r11 = 0
            g11 = 0
            b11 = 255
        np[11] = (r11, g11, b11)
    np.show()

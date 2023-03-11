from IRM import *
from microbit import *
from iled4 import *
import time
import music
pin12.set_pull(pin12.PULL_UP)
f = iled4()
d = IRM()
digit = 0
num0 = 0
num1 = 0
num2 = 0
num3 = 0
hr = 0
minute = 0
while 1:
    key = d.get(pin12)
    if key != -1:
        if key == 14:
            hr = (num0 * 10) + num1
            minute = (num2 * 10) + num3
            while hr > 0 or minute > 0:
                sleep(100)
                # time.sleep(60)  # delay 60 Sec
                minute -= 1
                if minute < 0 and hr > 0:
                    minute = 59
                    hr -= 1
                f.print((hr * 100) + minute)
                f.set_colon()
                f.update_display()
                if minute == 0 and hr == 0:
                    display.show(Image.HAPPY)
                    music.play(music.DADADADUM)
                    break
        elif key == 8:
            digit = digit + 1
            if digit > 3:
                digit = 0
            print(digit)
        elif key == 10:
            digit = digit - 1
            if digit < 0:
                digit = 3
            print(digit)
        else:
            pass
        if digit == 0:
            if key == 1:
                num0 += 1
                if num0 > 9:
                    num0 = 0
                print(num0)
            elif key == 9:
                num0 -= 1
                if num0 < 0:
                    num0 = 9
                print(num0)
        elif digit == 1:
            if key == 1:
                num1 += 1
                if num1 > 9:
                    num1 = 0
                print(num1)
            elif key == 9:
                num1 -= 1
                if num1 < 0:
                    num1 = 9
                print(num1)
        elif digit == 2:
            if key == 1:
                num2 += 1
                if num2 > 5:
                    num2 = 0
                print(num2)
            elif key == 9:
                num2 -= 1
                if num2 < 0:
                    num2 = 5
                print(num2)
        elif digit == 3:
            if key == 1:
                num3 += 1
                if num3 > 9:
                    num3 = 0
                print(num3)
            elif key == 9:
                num3 -= 1
                if num3 < 0:
                    num3 = 9
                print(num3)
    else:
        pass
    f.print((num0*1000) + (num1*100) + (num2*10) + num3)
    f.set_colon()
    f.update_display()

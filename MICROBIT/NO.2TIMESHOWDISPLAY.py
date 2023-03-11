# Write your code here :-)
from microbit import *

import tm1637

tm = tm1637.TM1637(clk=pin15, dio=pin16)
Sec = 30
Min = 10

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        sleep(100)
        while Sec > 0 or Min > 0:
            Sec -= 1
            if Sec < 0 and Min > 0:
                Sec = 59
                Min -= 1
            tm.numbers(Min, Sec)
            sleep(1000)

        if Sec == 0 and Min == 0:
            display.show(Image.HAPPY)
            pin0.write_digital(1)
            sleep(1000)
            pin0.write_digital(0)
            display.clear()

    if button_a.is_pressed():
        sleep(100)
        Min = Min + 1
        if Min > 59:
            Min = 0

    if button_b.is_pressed():
        sleep(100)
        Sec = Sec + 1
        if Sec > 59:
            Sec = 0
            Min += 1
        if Min > 59:
            Min = 0
            Sec = 0

    display.clear()
    tm.numbers(Min, Sec)

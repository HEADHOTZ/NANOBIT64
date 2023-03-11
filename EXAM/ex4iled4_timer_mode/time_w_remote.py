from IRM import *
from microbit import *
from iled4 import *
import time
import music

f = iled4()
pin12.set_pull(pin12.PULL_UP)
d = IRM()
number = {12: 0, 16: 1, 17: 2, 18: 3, 20: 4, 21: 5, 22: 6, 24: 7, 25: 8, 26: 9}
hr = 0
hr_left = 0
hr_right = 0
minute = 0
minute_left = 0
minute_right = 0
state = None
digit_state = None
mode = None
while 1:
    key = d.get(pin12)
    # ใช้ปุ่มฟังค์ชั่นในการเลือกว่าจะปรับชั่วโมงหรือนาที
    if key != -1:  # เวลาทำเกี่ยวกับ IR remote ถ้าสั่งการอะไรต้องอยู่ภายใต้ if key != -1
        if key == 14:
            hr = (hr_left * 10) + hr_right
            minute = (minute_left * 10) + minute_right
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
        elif key == 2:
            state = 0
            display.clear()
            print("choose mode")
        elif key == 5:
            state = 1
            print("select mode")
        else:
            pass
            # เลือกโหมดว่าจะชั่วโมงหรือนาที
        if state == 0:
            if key == 4:
                mode = 0  # mode Hour
                display.show("H")
            elif key == 6:
                mode = 1  # mode Minute
                display.show("M")
            else:
                pass
        # ปรับเวลา
        elif state == 1:  # ถ้าเลือกการปรับเวลา
            if mode == 0:  # ถ้าเลือก Hour mode
                # เลือกปรับตัวซ้ายขวา
                if key == 4:  # ถ้ากดเลือกซ้าย
                    digit_state = 0  # สถานะของ digit
                    print("Digit left")
                elif key == 6:  # ถ้ากดเลือกขวา
                    digit_state = 1  # สถานะของ digit
                    print("Digit right")
                else:
                    pass
                if digit_state == 0:
                    # if key != -1:
                    if key in number:
                        hr_left = number[key]
                        print(number[key])
                elif digit_state == 1:
                    # if key != -1:
                    if key in number:
                        hr_right = number[key]
                        print(number[key])
                else:
                    pass
            elif mode == 1:  # ถ้าเลือก Minute mode
                # เลือกปรับตัวซ้ายขวา
                if key == 4:  # ถ้ากดเลือกซ้าย
                    digit_state = 0  # สถานะของ digit
                    print("Digit left")
                elif key == 6:  # ถ้ากดเลือกขวา
                    digit_state = 1  # สถานะของ digit
                    print("Digit right")
                else:
                    pass
                if digit_state == 0:
                    # if key != -1:
                    if key in number:
                        minute_left = number[key]
                        if minute_left > 5:
                            minute_left = 0
                        print(number[key])
                elif digit_state == 1:
                    # if key != -1:
                    if key in number:
                        minute_right = number[key]
                        print(number[key])
                else:
                    pass
            else:
                pass
        else:
            pass
    f.print((hr_left * 1000) + (hr_right * 100) + (minute_left * 10) + minute_right)
    f.set_colon()
    f.update_display()

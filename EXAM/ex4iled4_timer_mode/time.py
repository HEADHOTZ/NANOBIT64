from microbit import *
from iled4 import *
import time
import music
import gc
gc.collect()
f = iled4()
hr = 0
minute = 0
sw_state = None
mode = None
while 1:
    if button_a.is_pressed() and button_b.is_pressed():
        while hr > 0 or minute > 0:
            time.sleep(60)  # delay 60 Sec
            minute -= 1
            if minute < 0 and hr > 0:
                minute = 59
                hr -= 1
            f.print((hr*100) + minute)
            f.set_colon()
            f.update_display()
            if minute == 0 and hr == 0:
                display.show(Image.HAPPY)
                music.play(music.DADADADUM)
                break
    # เลือกโหมดถ้ากดปุ่ม A จะเลือกว่าจะปรับชั่วโมงหรือนาที ปุ่ม B คือตั้งเวลา
    elif button_a.is_pressed():
        display.clear()
        sw_state = 0
    # ปุ่ม B ปรับเวลา
    elif button_b.is_pressed():
        sw_state = 1
    else:
        pass
        # เลือกโหมดว่าจะชั่วโมงหรือนาที
    if sw_state == 0:
        if not pin8.read_digital():
            mode = 0
            display.show('H')
        elif not pin12.read_digital():
            mode = 1
            display.show('M')
        else:
            pass
    elif sw_state == 1:
        # Hr mode
        if mode == 0:
            if not pin8.read_digital():
                while not pin8.read_digital():
                    sleep(10)
                hr += 1
            elif not pin12.read_digital():
                while not pin12.read_digital():
                    sleep(10)
                hr -= 1
                if hr < 0:
                    hr = 0
            # print(hr)
        # Minute mode
        if mode == 1:
            if not pin8.read_digital():
                while not pin8.read_digital():
                    sleep(10)
                minute += 1
                if minute > 59:
                    minute = 0
                    hr += 1
            if not pin12.read_digital():
                while not pin12.read_digital():
                    sleep(10)
                minute -= 1
                if minute < 0:
                    minute = 59
                    hr -= 1
            # print(minute)
    else:
        pass
    f.print((hr*100) + minute)
    f.set_colon()
    f.update_display()

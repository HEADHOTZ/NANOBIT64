# บอร์ด1 F:
from microbit import *
from microbit import sleep

from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
import radio

initialize()
clear_oled()

radio.on()
radio.config(channel=42)
radio.config(power=7)

i2c.init(freq=100000, sda=pin20, scl=pin19)
addr = 0x23

CH1 = 0
CH2 = 0
dat = 0
# บอร์ด1 F:
while True:
    x = radio.receive()
    VR = pin2.read_analog()
    sleep(120)

    if button_a.was_pressed():
        CH1 = 1
        CH2 = 0

    if button_b.was_pressed():
        CH1 = 0
        CH2 = 1

    if CH1 == 1:
        msg1 = "V, {}".format(VR)
        radio.send(msg1)
        clear_oled()
        display.show("V")

    if CH2 == 1:
        # ส่ง L
        msg2 = 'L'
        radio.send(msg2)
        display.show('L')
        # รับค่าจากบอร์ด3
        if x != None:
            dat = x.split(",")
            x1 = (dat[0])
            lux = float(x1)
            add_text(0, 2, "LUX = " + str(lux))
    sleep(10)

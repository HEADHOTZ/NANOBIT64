from microbit import *
import radio
radio.on()

radio.config(channel=42)
radio.config(power=7)

Num = 0
Number = ''

while True:
    x = pin2.read_analog()
    if button_a.was_pressed():
        Num += 1
        if Num > 6:
            Num = 0
    msg = "{}, {}".format(Num, x)
    # msg = "{},{}".format(Num, x)
    # sleep(500)
    radio.send(msg)
    # sleep(500)
    display.scroll(Num + 1, 100)


from microbit import *
import radio
radio.on()
radio.config(channel = 42)
radio.config(power = 7)
dat = 0
x1 = ''
x2 = ''
# บอร์ด 2 E:
def servo(pin, degrees):
    degrees = max(0, min(degrees, 180))
    duty = degrees / 180 * 102 + 25
    pin.write_analog(duty)

while True:
    x = radio.receive()
    if x != None:
        dat = x.split(",")
        x1 = (dat[0])
        if x1 == 'V':
            x2 = (dat[1])

    if x1 == 'V':
        VR = int(x2) * 180 / 1023
        servo(pin12, VR)
        display.show(x1)
    else:
        display.clear()

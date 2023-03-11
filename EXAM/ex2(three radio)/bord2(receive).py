from microbit import *
import radio

radio.on()
radio.config(channel=42)
radio.config(power=7)

command = None

dat = 0

Msg = ""

def servo(pin, degrees):
    degrees = max(0, min(degrees, 180))
    duty = degrees / 180 * 102 + 25
    pin.write_analog(duty)

while 1:
    x = radio.receive()
    if x != None:
        dat = x.split()
        x1 = (dat[0])
        x2 = (dat[1])

    if command == 1:
        x2 = (dat[1])
        if x1 == "as":
            if int(x2) > 180:
                print(x2, "Out of range")
            servo(pin8, int(x2))
            print("Servo =", x2)
        else:
            pass


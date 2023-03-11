from microbit import *
import radio
import neopixel

np = neopixel.NeoPixel(pin10, 12)

radio.on()
radio.config(channel=42)
radio.config(power=7)
x1 = ''  # receive Num from bord 1
x2 = ''  # receive Analog from bord 2
dat = 0

color = [
    (255, 255, 255),
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 0),
    (128, 0, 255),
    (255, 128, 0),
    (0, 255, 255),
]

while 1:
    x = radio.receive()
    # dat[0] = bn
    # dat[1] = Num
    # dat[2] = Analog

    if x != None:
        dat = x.split(",")
        x1 = int(dat[1])  # receive Num from bord 1
        x2 = int(dat[2])  # receive Analog from bord 1
        y = x2 * 12 / 1021
        print(x2)
        if x[0:2] == "bn":
            # led on
            for i in range(0, y):
                np[i] = color[x1]
            # shut down led
            for i in range(12, y, -1):
                np[i] = (0, 0, 0)
            np.show()
# Drive E-------------------------------------------

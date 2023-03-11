from microbit import *
import radio
import neopixel

radio.on()

radio.config(channel=42)
radio.config(power=7)


np = neopixel.NeoPixel(pin10, 16)
x1 = ''  # receive Num from bord 1
x2 = ''  # receive Analog from bord 2
dat = 0
color = [(255, 255, 255), (255, 0, 0), (255, 255, 0),
        (0, 255, 0), (128, 0, 255), (255, 128, 0),
        (0, 255, 255)]
while True:
    x = radio.receive()
    # sleep(500)
    if x != None:
        dat = x.split(",")
        x1 = int(dat[0])  # receive Num from bord 1
        x2 = int(dat[1])  # receive Analog from bord 2
        y = x2 / 64

        # led on
        for i in range(0, y):
            np[i] = color[x1]
        # shut down led
        for i in range(15, y, -1):
            np[i] = (0, 0, 0)
        np.show()
        display.scroll(x1 + 1, 100)


from microbit import *
import neopixel
np = neopixel.NeoPixel(pin16, 16)
Num = 0
color = [(255, 255, 255), (255, 0, 0), (255, 255, 0),
        (0, 255, 0), (128, 0, 255), (255, 128, 0),
        (0, 255, 255)]
while True:
    x = pin2.read_analog()
    y = int(x/64)

    if button_a.was_pressed():
        Num += 1
        if Num > 6:
            Num = 0
    display.show(Num + 1)

    # led on
    for i in range(0, y):
        np[i] = color[Num]
    # shut down led
    for i in range(15, y, -1):
        np[i] = (0, 0, 0)
    np.show()


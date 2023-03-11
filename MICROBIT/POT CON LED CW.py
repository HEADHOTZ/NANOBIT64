from microbit import *

X = 0
Y = 0

while True:
    VR1 = pin2.read_analog()
    VAL = pin2.map(VR1, 0, 1023, 0, 5)
    display.scroll(str(VAL))
    sleep(1000)

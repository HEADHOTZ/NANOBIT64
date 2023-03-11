from microbit import *
from IRM import *
pin12.set_pull(pin12.PULL_UP)
d = IRM()
X = ''
while 1:
    key=d.get(pin12)
    if(key!=-1):
        if key == 12:
            X = '0'
        elif key == 16:
            X = '1'
        elif key == 17:
            X = '2'
        elif key == 18:
            X = '3'
        elif key == 20:
            X = '4'
        elif key == 21:
            X = '5'
        elif key == 22:
            X = '6'
        elif key == 24:
            X = '7'
        elif key == 25:
            X = '8'
        elif key == 26:
            X = '9'
    display.show(X)
    print(key)

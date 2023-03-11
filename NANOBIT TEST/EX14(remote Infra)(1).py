from microbit import *
from IRM import *
from microbit import pin12
pin12.set_pull(pin12.PULL_UP)
d = IRM()
X = ''
while True:
    key=d.get(pin12)
    # รีโมทคนละความถี่เลยเขียนแบบนี้
    if(key!=-1):
        if key == 22:
            X = '0'
        elif key == 12:
            X = '1'
        elif key == 24:
            X = '2'
        elif key == 94:
            X = '3'
        elif key == 8:
            X = '4'
        elif key == 28:
            X = '5'
        elif key == 90:
            X = '6'
        elif key == 66:
            X = '7'
        elif key == 82:
            X = '8'
        elif key == 74:
            X = '9'
    display.show(X)
    print(key)

from microbit import *
import radio
radio.on()
while True:
#ส่ง
    if button_a.was_pressed():
        radio.send('A')
    elif button_b.was_pressed():
        radio.send('B')
#รับ
    x=radio.receive()
    if x=='A':
        display.show(Image.HEART,clear=True)
    elif x=='B':
        display.show(Image.DUCK,clear=True)

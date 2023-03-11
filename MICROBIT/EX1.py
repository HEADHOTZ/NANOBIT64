from microbit import *

p11 = Image("00000:" 	
            "00000:"
            "00900:"
            "00000:"
            "00000")

p12 = Image("99999:" 	
            "96669:"
            "96369:"
            "96669:"
            "99999")

while True:
    if button_a.is_pressed() and not button_b.was_pressed():
        display.show(Image.DIAMOND)
        sleep(500)
        display.show(Image.DIAMOND_SMALL)
        sleep(500)
        display.show(p11)
        sleep(500)
        display.clear()

    if button_b.is_pressed()and not button_a.was_pressed():
        display.show(p12)

    if button_a.was_pressed() and button_b.was_pressed():
        display.clear()
        for y in range(0,5):
            for x in range(0,5):
                display.set_pixel(x,y,9)
                sleep(200)
        for y in range(0,5):
            for x in range(0,5):
                display.set_pixel(x,y,0)
                sleep(200)


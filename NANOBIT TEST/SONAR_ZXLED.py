from microbit import *
import music
import gc
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
initialize()
clear_oled()
gc.collect()
while 1:
    ultra = (pin1.read_analog()/10)
    if ultra <= 5:
        pin8.write_digital(1)
        music.pitch(2000,100)
    else:
        pin8.write_digital(0)
    print(ultra)
    add_text(0, 0,"Samutprakan")
    add_text(0, 1,"Technical")
    add_text(0, 2,"College")
    add_text(0, 3,"{0:.1f}".format(ultra))
    # add_text(0, 3,str(ultra))
    sleep(500)

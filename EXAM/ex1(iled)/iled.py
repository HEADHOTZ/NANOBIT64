from microbit import *
class iled:
    ADDRESS             = 0x70
    BLINK_CMD           = 0x80
    CMD_BRIGHTNESS      = 0xE0
    # Digits 0 - F
    NUMS = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20] # Default

    def __init__(self):
        self.buffer = bytearray([0]*16)
        i2c.write(self.ADDRESS,b'\x21')
        # 0 to 3
        self.blink_rate(0)
        # 0 to 15
        self.set_brightness(15)
        self.update_display()

    def set_brightness(self,b):
        i2c.write(self.ADDRESS,bytes([self.CMD_BRIGHTNESS | b]))

    def blink_rate(self, b):
        i2c.write(self.ADDRESS,bytes([self.BLINK_CMD | 1 | (b << 1)]))

    def write_digit(self, position, digit, dot=False):
        # skip the colon
        offset = 0 #if position < 2 else 1
        pos = offset + position
        self.buffer[pos*2] = self.NUMS[digit] & 0xFF
        if dot:
            self.buffer[pos*2] |= 0x80

    def update_display(self):
        data = bytearray([0]) + self.buffer
        i2c.write(self.ADDRESS,data)

    def clear(self):
        self.buffer = bytearray([0]*16)
        self.update_display()


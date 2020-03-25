
import time
from grove.gpio import GPIO

__all__ = ['GroveLed', 'GPIO']

class GroveLed(GPIO):
    '''
    Class for Grove - XXXX Led

    Args:
        pin(int): number of digital pin the led connected.
    '''
    def __init__(self, pin):
        super(GroveLed, self).__init__(pin, GPIO.OUT)

    def on(self):
        '''
        light on the led
        '''
        self.write(1)

    def off(self):
        '''
        light off the led
        '''
        self.write(0)


Grove = GroveLed


def main():
# from grove.helper import SlotHelper
#  sh = SlotHelper(SlotHelper.GPIO)
# pin = sh.argv2pin()

    led = GroveLed(24)

    while True:
        led.on()
        time.sleep(10)
        led.off()
        time.sleep(3)


if __name__ == '__main__':
    main()


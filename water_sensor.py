import math
import sys
import time
from grove.adc import ADC


class GroveWaterSensor:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        return self.adc.read(self.channel)

Grove = GroveWaterSensor


def main():
   # if len(sys.argv) < 2:
   #     print('Usage: {} adc_channel'.format(sys.argv[0]))
   #     sys.exit(1)

    sensor = GroveWaterSensor(2)

    print('Detecting ...')
    while True:
        wvalue = sensor.value
        if sensor.value < 200:
            print("{}, Detected Water.".format(wvalue))
        else:
            print("{}, Dry.".format(wvalue))

        time.sleep(.1)

def water():
    
    
    sensor = GroveWaterSensor(2)

    print('Detecting ...')
    wvalue = sensor.value
    if sensor.value < 200:
            #print("{}, Detected Water.".format(wvalue))
        return "{}, Detected Water.".format(wvalue)
    else:
            #print("{}, Dry.".format(wvalue))
        return "{}, Dry.".format(wvalue)
    #time.sleep(1)

def water_v():

    sensor = GroveWaterSensor(2)

   # print('Detecting ...')
    wvalue = sensor.value
    return wvalue
   # time.sleep(1)



if __name__ == '__main__':
    main()
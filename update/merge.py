import math
import sys
import time
from grove.adc import ADC
import dht11
import seeed_dht

__all__ = ["GroveMoistureSensor"]

class GroveMoistureSensor:
    '''
    Grove Moisture Sensor class\

    Args:
        pin(int): number of analog pin/channel the sensor connected.
    '''
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def moisture(self):
        '''
        Get the moisture strength value/voltage

        Returns:
            (int): voltage, in mV
        '''
        value = self.adc.read_voltage(self.channel)
        return value

Grove = GroveMoistureSensor


def main():
    sensor = seeed_dht.DHT("11", 12)

   #  from grove.helper import SlotHelper
   # sh = SlotHelper(SlotHelper.ADC)
   # pin = sh.argv2pin()

    sensor1 = GroveMoistureSensor(0)

    print('Detecting moisture...')
    while True:
        m = sensor1.moisture
        humi, temp = sensor.read()
        print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))
        if 0 <= m and m < 300:
            result = 'Dry'
        elif 300 <= m and m < 600:
            result = 'Moist'
        else:
            result = 'Wet'
        print('Moisture value: {0}, {1}'.format(m, result))
        print('DHT{0}, humidity & temperature: {1}'.format(sensor.dht_type, temp))
        time.sleep(1)

if __name__ == '__main__':
    main()
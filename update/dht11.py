import time
import seeed_dht


def dht11():    # for DHT11/DHT22
    sensor = seeed_dht.DHT("11", 12)
    # for DHT10
    # sensor = seeed_dht.DHT("10")

    while True:
        humi, temp = sensor.read()
        if not humi is None:
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(sensor.dht_type, temp))
        time.sleep(1)
        
def getDht():
    sensor = seeed_dht.DHT("11", 12)
    humi, temp = sensor.read()
    result = ''
    if not humi is None:
        result = 'DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp)
    else:
        result = 'DHT{0}, humidity & temperature: {1}'.format(sensor.dht_type, temp)
        
    return result
    


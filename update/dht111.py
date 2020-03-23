import time
import moisture
import water_sensor
import dht11 as dht


while True:
    
    #dht.dht11()
    print(dht.getDht())
    time.sleep(1)
    
    print(moisture.getData())
    time.sleep(1)
    
    print(water_sensor.getdata())
    time.sleep(1)
    
    
#    if not humi is None:
 #       print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))
 #   else:
 #       print('DHT{0}, humidity & temperature: {1}'.format(sensor.dht_type, temp))
        
        
        
        
#        if 0 <= m and m < 300:
#            result = 'Dry'
#        elif 300 <= m and m < 600:
#            result = 'Moist'
#        else:
#            result = 'Wet'
#        print('Moisture value: {0}'.format(m))
#        time.sleep(1)

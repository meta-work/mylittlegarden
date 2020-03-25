from pyfirmata import Arduino, util
import time


ardu = Arduino('/dev/ttyACM0')

#input = ardu.get_pin('d:8:i')
test_led = ardu.get_pin('d:13:o')
water_pump = ardu.get_pin('d:7:o')
led_12v = ardu.get_pin('d:8:o')

#시리얼 값 반복 + 반복자 스레드
st == util.Iterator(ardu)
st.start()
#input 리포팅 활성화
#input.enable_reporting()

while True:
    if sw.read():
        led_12v.write(1)
    if else:
        water_pump.write(1)
    time.sleep(1)
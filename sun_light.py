import time
import SI1145.SI1145 as SI1145

sensor = SI1145.SI1145()

#while True:
vis = sensor.readVisible()
IR = sensor.readIR()
UV = sensor.readUV()
uvIndex = UV / 100.0

print( 'Vis:             ' + str(vis))
print( 'IR:              ' + str(IR))
print('UV Index:        ' + str(uvIndex))

time.sleep(1)

def sun_light():
        vis = sensor.readVisible()
        IR = sensor.readIR()
        UV = sensor.readUV()
        uvIndex = UV / 100.0
        return 'Vis:             ' + str(vis)
        return 'IR:              ' + str(IR)
        return 'UV Index:        ' + str(uvIndex)

        #time.sleep(1)

def sun_light_v():

        vis = sensor.readVisible()
        IR = sensor.readIR()
        UV = sensor.readUV()
        uvIndex = UV / 100.0

        result = str(vis) ,str(IR) , str(uvIndex)
        return result

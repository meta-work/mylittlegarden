import time
import dht11 as dht
import moisture
import water_sensor
from flask import Flask , jsonify

#count = 0

app = Flask(__name__)

@app.route('/')
def home():
  #  global count
  #  count += 1
    return jsonify(
        dht.getDht(),moisture.getData(),water_sensor.getdata()
        #     count=count
    )

#@app.route('/abuse')
#def abuse_count():
#    global count
#    count += 100
#    return ''
    
    
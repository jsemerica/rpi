#!/usr/bin/python3

import Adafruit_DHT
from time import sleep 
import sys
from urllib.request import urlopen

myAPI = 'AWE52J15SYSO4ANM'

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17 

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

#    if humidity is not None and temperature is not None:
  temperature = '%.3f' % temperature
  humidity = '%.3f' % humidity
  temp_c = float(temperature)
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  print(temp_f, humidity)

  conn = urlopen(baseURL + '&field1=%s&field2=%s' % (temp_f, humidity))
  conn.read()
  conn.close()

#    else:
#        print("Failed to retrieve data from humidity sensor")

  sleep(10)

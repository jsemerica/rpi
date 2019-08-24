#!/usr/bin/python3

import io
from time import sleep
from urllib.request import urlopen

myAPI = 'AWE52J15SYSO4ANM'

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI


while True:

  tFile = open('/sys/class/thermal/thermal_zone0/temp')
  temp = float(tFile.read())
  tempC = temp/1000

  if ( tempC < 72 ):
    print ("cold", tempC)
  else:
    print ("hot", tempC)

#  conn = urlopen(baseURL + '&field5=%s' % tempC)
#  conn.read()
#  conn.close()


  sleep(2)

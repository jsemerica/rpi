#!/usr/bin/python3

import io
from time import sleep


while True:

  tFile = open('/sys/class/thermal/thermal_zone0/temp')
  temp = float(tFile.read())
  tempC = temp/1000
 
  print (tempC)

  sleep(5)

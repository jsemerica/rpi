#!/usr/bin/python

import glob
import time
import datetime
import urllib2
import sys

myAPI = 'AWE52J15SYSO4ANM'

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

device1 = '/sys/bus/w1/devices/28-01144b4ed6aa/w1_slave'
device2 = '/sys/bus/w1/devices/28-01144c54f7aa/w1_slave'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

def read_temp_raw_device1():
    f = open(device1, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp_raw_device2():
    f = open(device2, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp_device1():
    lines = read_temp_raw_device1()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw_device1()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f_device1 = temp_c * 9.0 / 5.0 + 32.0

        return temp_f_device1

def read_temp_device2():
    lines = read_temp_raw_device2()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw_device2()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f_device2 = temp_c * 9.0 / 5.0 + 32.0

        return temp_f_device2


while True:
    now = datetime.datetime.now()
    temp1 = read_temp_device1()
    temp2 = read_temp_device2()

    temp1f = '%.1f' % temp1
    temp2f = '%.1f' % temp2

#    conn = urllib2.urlopen(baseURL + '&field3=%s' % temp)
    conn = urllib2.urlopen(baseURL + '&field3=%s&field4=%s' % (temp1f, temp2f))
    print conn.read()
    conn.close()

    print now.isoformat(),read_temp_device1(),read_temp_device2()
    time.sleep(30)


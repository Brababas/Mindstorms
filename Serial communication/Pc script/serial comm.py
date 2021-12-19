# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:19:02 2021

@author: baert
"""

import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'
ser.open()

if ser.is_open: 
    print("Serial port is opened")
    
# ser.write(str.encode("test"))
message = ser.readline()
message = message.decode()
firstpart = message.split(":",1)[0]
print(firstpart)
ser.close()

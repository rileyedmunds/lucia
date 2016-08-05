"""
ldr.py

EXECUTION:

python3 plot.py --port /dev/tty.usbmodem1411

"""
#import webcam python file:
from webcam import video


import sys, serial, argparse
import numpy as np
from time import sleep

import matplotlib.pyplot as plt 
import matplotlib.animation as animation

strPort = '/dev/tty.usbmodem1411'
ser = serial.Serial(strPort, 9600, timeout = None, xonxoff=False, rtscts=False, dsrdtr=False)
print(ser)


#LOOP:
while True:
  bytesToRead = ser.inWaiting()
  # print(bytesToRead)
  if (bytesToRead > 0):
    next = ser.read(bytesToRead)
    string = next.decode("utf-8") 
    print(string)
    if "1" in string:
      print("MOTION!!!")
      video('haarcascade_frontalface_default.xml')
      break;
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
serie.py

Script para la comunicación por medio de puerto serie con el Arduino monitor del sistema

"""

import serial
import time

PORT = '/dev/ttyACM0'
BAUD = 115200
TIMEOUT = 0.01

ser = serial.Serial()

def open():
  print 'Iniciando Arduino...'
  print 'Configurando conexión serie: \nPuerto: '+PORT+'\nBaudrate: '+str(BAUD)+'\nTimeout: '+str(TIMEOUT)
  ser.port = PORT
  ser.baudrate = BAUD
  ser.timeout = TIMEOUT
  ser.open() 

  time.sleep(4)

def close():
  ser.close()



def setConfig(port=PORT, baud=BAUD, timeout=TIMEOUT):
  ser.port = port
  ser.baudrate = baudrate
  ser.timeout = timeout

def getConfig():
  return {'port':ser.port, 'baudrate':ser.baudrate, 'timeout':ser.timeout}




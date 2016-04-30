import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
class Sensor:
	__instance = None
	@staticmethod
	def getInstance():
		if Sensor.__instance is None:
			GPIO.setwarnings(False)
			GPIO.setmode(GPIO.BCM)
			GPIO.cleanup()
			Sensor.__instance=dht11.DHT11(pin=23)
		return Sensor.__instance

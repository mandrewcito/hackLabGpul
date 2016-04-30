import dht11
import RPi.GPIO as GPIO
import sensor
import exceptions
class Humidity:
	def getData(self):
		aux=sensor.Sensor.getInstance().read()
		if not (aux.is_valid()):
			raise NameError('Error')
			return
		return aux.humidity

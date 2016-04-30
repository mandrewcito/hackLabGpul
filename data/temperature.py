import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

class Temperature:
	__instance=None
	def __init__(self):
		if Temperature.__instance is None:
			Temperature.__instance=BMP085.BMP085()
	def getData(self):
		return Temperature.__instance.read_temperature()

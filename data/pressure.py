import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

class Pressure:
	__instance=None
	def __init__(self):
		if Pressure.__instance is None:
			Pressure.__instance=BMP085.BMP085()
	def getData(self):
		return Pressure.__instance.read_pressure()
				

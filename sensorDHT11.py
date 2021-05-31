import time
import board
import adafruit_dht


class Tools(object):
	dhtDevice = adafruit_dht.DHT11(board.D17)
	def sensorHumedadYTemperatura(self):
		try:
			temperature_c = self.dhtDevice.temperature
			temperature_f = temperature_c * (9 / 5) + 32
			humidity = self.dhtDevice.humidity
			'''print(
			    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
				temperature_f, temperature_c, humidity
			    )
			)'''
			return [temperature_c, humidity]
		except RuntimeError as error:
			#print(error.args[0])
			time.sleep(2.0)
		except Exception as error:
			dhtDevice.exit()
			raise error

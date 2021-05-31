import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
TRIG = 4
ECHO = 18
 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

class Tools(object):
	def sensorUltrasonico(self):
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		 
		while GPIO.input(ECHO) == False:
			start = time.time()
		 
		while GPIO.input(ECHO) == True:
			end = time.time()
		 
		sig_time = end-start
		 
		#CM:
		distance = sig_time / 0.000058
		 
		#inches:
		#distance = sig_time / 0.000148
		return distance
		#print('Distance: %.2f cm' %distance)

'''	 
while True:
	print('Distance: %.2f cm' %sensorUltrasonico())
	time.sleep(1)
'''	
#GPIO.cleanup()


import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)	

def showcase():
	duty1 = 90 / 10 + 2.5
	duty2 = 0 / 10 + 2.5
	duties = [duty1, duty2, duty1, duty2, duty1]
	for d in duties:
		pwm.ChangeDutyCycle(d)
		time.sleep(2)

#def main():
#	print "90 = relax"
#	print "0 = flex"
#	input = raw_input()
#	duty = float(input) / 10.0 + 2.5
#	pwm.ChangeDutyCycle(duty)
#	time.sleep(1.1)
#	main()


#main()
showcase()

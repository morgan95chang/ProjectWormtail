#set all servos to ZERO position
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#setup ports
ports = [18,23,25,22,4]
for outport in ports:
	GPIO.setup(outport,GPIO.OUT)

#initiate hand
thumb = GPIO.PWM(18, 100)
index = GPIO.PWM(23, 100)
middle = GPIO.PWM(25, 100)
ring = GPIO.PWM(22, 100)
pinky = GPIO.PWM(4, 100)
hand = [thumb, index, middle, ring, pinky]

#vars
full = 0 / 10 + 2.5
moster = 13 / 10 + 2.5
most = 45 / 10 + 2.5 
half = 90 / 10 + 2.5
zero = 180 / 10 + 2.5

#prompt for command
def prompt():
	print "<J> to zero (0*)"
	print "<K> for half (90*)"
	print "<L> for most (135*)"
	print "<;> for full (180*)"
	print "<exit> to quit"
	command = raw_input("Enter command: ")
	digested = readInput(command)
	gesture(digested)
	time.sleep(1)
	prompt()

#translate raw input
def readInput(command):
	g = []
	if (command == "exit"):
		setZero()
		GPIO.cleanup()
		print "Goodbye"
		sys.exit()
	for c in command:
		if (c == ("j" or "J")):
			g.append(0)
		if (c == ("k" or "K")):
			g.append(1)
		if (c == ("l" or "L")):
			g.append(2)
		if (c == ";"):
			g.append(3)
	return g

#gesture
def gesture(gest):
	for g in gest:	
		time.sleep(1)
		for finger in hand:
			if (g == 0):	#0* zero
				time.sleep(0.75)
				finger.ChangeDutyCycle(zero)
			if (g == 1):	#90* half
				time.sleep(0.75)
				finger.ChangeDutyCycle(half)
			if (g == 2):	#135* most
				time.sleep(0.75)
				finger.ChangeDutyCycle(most)
			if (g == 3): 	#180* full
				time.sleep(0.75)
				finger.ChangeDutyCycle(full)
				
#final zero
def setZero():
	for finger in hand:
		finger.ChangeDutyCycle(zero)

#main function
def main():
	for finger in hand:
		finger.start(zero)
	print "Welcome to Project Wormtail"
	prompt()

main()

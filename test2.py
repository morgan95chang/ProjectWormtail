#control of individual and groups of fingers via keyboard

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
thumb = GPIO.PWM(4, 100)
index = GPIO.PWM(22, 100)
middle = GPIO.PWM(25, 100)
ring = GPIO.PWM(23, 100)
pinky = GPIO.PWM(18, 100) 
hand = [thumb, index, middle, ring, pinky]

#vars
relax = 180 / 10 + 2.5
flex1 = 90 / 10 + 2.5
flex2 = 45 / 10 + 2.5
flex3 = 35 / 10 + 2.5
flex4 = 0 / 10 + 2.5

#prompt for command
def prompt():
	print "Enter your command"
	print "Use a <SPACE> to separate gestures"
	print "	<H> for thumb"
	print "	<J> for index"
	print "	<K> for middle"
	print "	<L> for fourth"
	print "	<;> for pinkie"
	print "<SHOWBOAT> for demo"
	print "	<exit> to quit"
	command = raw_input("Enter command: ")
	digested = readInput(command)
	gesture(digested)
	time.sleep(1)
	clear()
	prompt()

#translate raw input
def readInput(command):
	clear()
	g = []
	if (command == "exit"):
		clear()
		GPIO.cleanup()
		print "Goodbye"
		sys.exit()
	if (command == ("showboat" or "SHOWBOAT")):
		g.append(18)
		g.append(0)
		g.append(23)
		g.append(0)
		g.append(25)
		g.append(0)
		g.append(22)
		g.append(0)
		g.append(4)
		g.append(0)
		g.append(22)
		g.append(0)
		g.append(25)
		g.append(0)
		g.append(23)
		g.append(0)
		g.append(18)
		g.append(0)
		g.append(18)
		g.append(23)
		g.append(25)
		g.append(22)
		g.append(4)
		g.append(0)
	for c in command:
		if (c == ("h" or "H")):
			g.append(18)
		if (c == ("j" or "J")):
			g.append(23)
		if (c == ("k" or "K")):
			g.append(25)
		if (c == ("l" or "L")):
			g.append(22)
		if (c == ";"):
			g.append(4)
		if (c == " "):
			g.append(0)
	return g

#gesture
def gesture(gest):
	for g in gest:	
		if (g == 0):
			time.sleep(1)
			clear()
			time.sleep(1)
		if (g == 18):
			thumb.ChangeDutyCycle(flex3)
		if (g == 23):
			index.ChangeDutyCycle(flex3)
		if (g == 25):
			middle.ChangeDutyCycle(flex3)
		if (g == 22):
			ring.ChangeDutyCycle(flex3)
		if (g == 4):
			pinky.ChangeDutyCycle(flex3)
			


#clears current gesture
def clear():
	for finger in hand:
		finger.ChangeDutyCycle(relax)
		
		
#main function
def main():
	for finger in hand:
		finger.start(relax)
	print "Welcome to Project Wormtail"
	prompt()

main()

import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ports = [18,23,25,22,4]

#prompt for command
def prompt():
	print "Enter your command"
	print "Use a <SPACE> to separate gestures"
	print "	<H> for thumb"
	print "	<J> for index"
	print "	<K> for middle"
	print "	<L> for fourth"
	print "	<;> for pinkie"
	print "	<exit> to quit"
	command = raw_input("Enter command: ")
	digested = readInput(command)
	gesture(digested)
	prompt()

#translate raw input
def readInput(command):
	clear()
	d = []
	if (command == "exit"):
		clear()
		GPIO.cleanup()
		print "Goodbye"
		sys.exit()
	for c in command:
		if (c == ("h" or "H")):
			d.append(18)
		if (c == ("j" or "J")):
			d.append(23)
		if (c == ("k" or "K")):
			d.append(25)
		if (c == ("l" or "L")):
			d.append(22)
		if (c == ";"):
			d.append(4)
		if (c == " "):
			d.append(0)
	return d

#gesture
def gesture(outports):
	for p in outports:	
		if (p == 0):
			time.sleep(1)
			clear()
		else:
			GPIO.output(p,GPIO.HIGH)

#clears current gesture
def clear():
	for port in ports:	
		GPIO.output(port,GPIO.LOW)
		
#main function
def main():
	#setup ports
	for outport in ports:
		GPIO.setup(outport,GPIO.OUT)
	print "Welcome to Project Wormtail"
	prompt()

main()

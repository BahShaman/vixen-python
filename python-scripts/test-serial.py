from ArduinoSerial import ArduinoSerial
import time

ard = ArduinoSerial()

while True:
	ard.send([0,0,0,0,0,0])
	time.sleep(1)
	ard.send([255,0,0,0,0,0])
	time.sleep(1)
	ard.send([255,255,0,0,0,0])
	time.sleep(1)
	ard.send([255,255,255,0,0,0])
	time.sleep(1)
	ard.send([255,255,255,255,0,0])
	time.sleep(1)
	ard.send([255,255,255,255,255,0])
	time.sleep(1)
	ard.send([255,255,255,255,255,255])
	time.sleep(1)



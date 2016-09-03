from ArduinoSerial import ArduinoSerial
import time
import pygame

ard = ArduinoSerial()
pygame.init()
i=0
while True:
	modchannel = [0,0,0,0,0,0,0,0]
	if int(i) > 0:
		modchannel[0] = 1
	if int(i) > 1:
		modchannel[1] = 1
	if int(i) > 2:
		modchannel[2] = 1
	if int(i) > 3:
		modchannel[3] = 1
	if int(i) > 4:
		modchannel[4] = 1
	if int(i) > 5:
		modchannel[5] = 1
	if int(i) > 6:
		modchannel[6] = 1
	if int(i) > 7:
		modchannel[7] = 1

		#done = True 
	print modchannel
	ard.send(modchannel)
	time.sleep(0.25)
	i = raw_input("enter input")	

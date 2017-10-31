#check files
import sys
sys.path.append('../vixen')
from vixen import Vixen
from ArduinoSerial import ArduinoSerial

ard = ArduinoSerial()
vix = Vixen()

print 'Running ArduinoProgram.py'

'''TODO: why issues with index'''
'''TODO: prevent multiple instances'''
vix.basedir('../VixenFiles')
files = vix.loadvixprogram(sys.argv[1])
#files = vix.loadvixprogram('HalloweenNight2013.vpr')

done = False
for file in files:
	vixfilename = file
	print 
	print 
	print file
	
	#vix.basedir('/home/pi/Github/vixen-python/VixenFiles')
	vix.loadfile(vixfilename)
	print vix.channels
	vix.processdata(vix.event_values,vix.channels)
	vix.set_screen((200,200))
	vix.play()
	per = 0
	while not done:
		if per >= vix.periods - 3:
			done = True
		vix.pos_syncwait(per)
		per += 1
		#print vix.periods, per
		ard.send(vix.period_arr(per))
		print vix.period_str(per)
		#pygame.display.flip()
		#if per % 100 == 0:
			#print '.', 
	ard.send([0,0,0,0,0,0])
	vix = None

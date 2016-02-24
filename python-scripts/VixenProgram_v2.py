#check files
from vixen import Vixen
from ArduinoSerial import ArduinoSerial

ard = ArduinoSerial()

print 'Running ArduinoProgram.py'

files = [
	'Arduino6ChannelPumpkinHeffalumpsA2-g.vix'
	,'Arduino6ChannelPumpkinGrinningGhosts.vix'
	,'Arduino6ChannelThisIsHolloweenMain.vix'
]
counter = 0

'''TODO: why issues with index'''
'''TODO: prevent multiple instances'''
while True:
	vixfilename = files[counter]
	counter ++
	counter = counter % len(files)
	print 
	print 
	print file
	vix = Vixen()
	vix.basedir('/home/pi/Github/vixen-python/VixenFiles')
	vix.loadfile(vixfilename)
	print vix.channels
	vix.processdata(vix.event_values,vix.channels)
	vix.set_screen((200,200))
	vix.play()
	done = False
	per = 0
	while not done:
		if per >= vix.periods - 3:
			done = True
		vix.pos_syncwait(per)
		per += 1
		#print vix.periods, per
		ard.send(vix.period_arr(per))
		#print vix.period_str(per)
		if per % 100 == 0:
			print '.', 
	ard.send([0,0,0,0,0,0])
	vix = None

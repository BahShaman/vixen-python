#check files
from vixen import Vixen
from ArduinoSerial import ArduinoSerial

ard = ArduinoSerial()

print 'Running ArduinoProgram.py'

files = [
#	'Arduino8ChannelChironBetaPrime.vix',
	'Arduino8ChannelChristmasIsComing.vix',
	'Arduino8ChannelChristmasLinusAndLucy.vix',
	'Arduino8ChannelDrummer.vix',
	'Arduino8ChannelOhChristmasTree.vix',
	'Arduino8ChannelSkating.vix',
#	'Arduino8ChannelZeldaMainTheme.vix',
]

'''TODO: why issues with index'''
'''TODO: prevent multiple instances'''
for file in files:
	vixfilename = file
	print 
	print 
	print file
	vix = Vixen()
	vix.basedir('/home/pi/github/vixen-python/VixenFiles')
	vix.loadfile(vixfilename)
	print vix.channels
	vix.processdata(vix.event_values,vix.channels)
	vix.set_screen((200,200))
	vix.play()
	done = False
	per = 0
	while not done:
		#for event in vix.pygame.event.get(): 
		#	if event.type == vix.pygame.QUIT: # If user clicked close
		#		done = True
		#	if event.type == vix.pygame.KEYDOWN: 
		#		if event.key == vix.pygame.K_ESCAPE:
		#			done = True 
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

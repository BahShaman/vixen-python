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
periods = 0
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
#	vix.set_screen((200,200))
	periods += vix.periods
	print periods
print "=================================="
print
print "Time: ",
print periods / 10 /60,
print "minutes",
print periods / 10 %60,
print "seconds"
print "periods",
print periods

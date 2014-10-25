#check files
from vixen import Vixen
from ArduinoSerial import ArduinoSerial

''' Test 1: full filename '''
print "============== Test 1 ================="
vixfilename = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Sequences\\Arduino8ChannelChristmasLinusAndLucy.vix"
musfile = 'C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Audio\\04-A Charlie Brown Christmas-Linus and Lucy.mp3'

vix = Vixen()
vix.loadfile(vixfilename)
vix.loadmusic(musfile)
vix.play()
vix = None


'''Test 2 relative file path'''
print "============== Test 2 ================="
vixfilename = "Arduino8ChannelChristmasLinusAndLucy.vix"
musfile = '04-A Charlie Brown Christmas-Linus and Lucy.mp3'

vix = Vixen()
vix.basedir('C:/Users/BOSCIA/Portable/Vixen 2.1.1.0')
vix.loadfile(vixfilename)
vix.loadmusic(musfile)
vix.play()
vix = None

'''Test 3 relative file path, get music from Sequence'''
print "============== Test 3 ================="
vixfilename = "Arduino8ChannelChristmasLinusAndLucy.vix"

vix = Vixen()
vix.basedir('C:/Users/BOSCIA/Portable/Vixen 2.1.1.0')
vix.loadfile(vixfilename)
vix.play()
vix = None

'''Test 4 check all files in a directory'''
print "============== Test 4 ================="
#raise BaseException("Test Not Implemented")
files = [
	'Arduino6ChannelThisIsHolloweenMain.vix'
	,'Arduino8ChannelChironBetaPrime.vix'
	,'Arduino8ChannelChristmasIsComing.vix'
	,'Arduino8ChannelChristmasLinusAndLucy.vix'
	,'Arduino8ChannelChristmasSample.vix'
	,'Arduino8ChannelDrummer.vix'
	,'Arduino8ChannelDrummer0.vix'
	,'Arduino8ChannelOhChristmasTree.vix'
	,'Arduino8ChannelPatterns.vix'
	,'Arduino8ChannelPatternsSample.vix'
	,'Arduino8ChannelPatternsSimon.vix'
	,'Arduino8ChannelSkating.vix'
	,'Arduino8ChannelTestSequence.vix'
	,'Arduino8ChannelZeldaMainTheme.vix'
]
for file in files:
	vixfilename = file
	print 
	print 
	print file
	vix = Vixen()
	vix.basedir('C:/Users/BOSCIA/Portable/Vixen 2.1.1.0')
	vix.loadfile(vixfilename)
	print vix.channels
	vix.processdata(vix.event_values,vix.channels)
	vix.set_screen((200,200))
	vix.play()
	done = False
	per = 0
	while not done:
		vix.pos_syncwait(per)
		per += 1
		#print vix.periods, per
		print vix.period_str(per)
		if per >= 100:
			done = True
		if per >= vix.periods:
			done = True
	vix = None

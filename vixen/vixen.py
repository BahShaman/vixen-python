import pygame
import os
import xml
import xml.etree.ElementTree as ET

class Vixen(object):
	screen = None
	data = ''
	has_musicfile = False
	has_vixfile = False
	has_profilefile = False
	basedirpath = ''
	defaultseqdir = 'Sequences/'
	defaultmusdir = 'Audio/'
	defaultprodir = 'Profiles/'
	vixfilename = ''
	musicfilename = ''
	channels = 1
	periods = 0
	permillis = 100
	sequence = []
	duration = 0
	title = 'Unnamed Sequence'
	serialOutput = False
	event_values = ''
	ticks_init = 0
	
	def __init__(self):
		pygame.init()
		"""http://www.raspberrypi.org/forums/viewtopic.php?f=2&t=1555"""
		#os.environ['SDL_VIDEODRIVER']="fbcon" # could be "directfb", try "aalib" for extra fun
	
	def __del__(self):
		try:
			pygame.mixer.music.stop()
		except:
			pass
	
	def set_screen(self,size):
		self.screen = pygame.display.set_mode(size)
		return self.screen
	
	def loadfilefromdir(self,dirname,vixfilename):
		"""load vixen file and set its base directories"""
		pass
	
	def loadfile(self,filename):
		self.loadvixfile(filename)
	
	def loadvixfile(self,vixfilename):
		"""---"""
		if self.basedirpath != '':
			print "Using base dir path %s" % self.basedirpath
			checkfilepath = self.basedirpath + '/' + self.defaultseqdir + vixfilename
		else:
			checkfilepath = vixfilename
		print "loading file %s" % checkfilepath
		if not os.path.exists(checkfilepath):
			raise BaseException("file not found")
		else:
			vixfilename = checkfilepath
			print "File %s found" % vixfilename
			tree = ET.parse(vixfilename)
			root = tree.getroot()
			#print root.tag
			#print root.find('Time').text
			self.permillis = root.find('EventPeriodInMilliseconds').text
			if len(root.find('Channels')) > 0:
				print "setting channels to %s" % len(root.find('Channels'))
				self.channels = len(root.find('Channels'))
			self.event_values = root.find('EventValues').text
			if root.find('Audio') is not None:
				tempmusicfilename = root.find('Audio').get('filename')
				print 'Attempting to load music file'
				self.loadmusic(tempmusicfilename)
				self.duration = root.find('Audio').get('duration')
				self.title = root.find('Audio').text
			if root.find('Profile') is not None:
				tempprofilename = root.find('Profile').text
				print 'Attempting to load profile file'
				self.loadvixprofile(tempprofilename)
			if root.find('PlugInData') is not None:
				pass
				PlugInData = root.find('PlugInData')[0]
				print PlugInData.get('name'),
				print PlugInData.get('enabled'),
				print PlugInData.get('from'),
				print PlugInData.get('to'),
				if PlugInData.get('name') == 'Generic serial':
					pass
					print PlugInData.find('Name').text,
					print PlugInData.find('Baud').text,
					print PlugInData.find('Parity').text,
					print PlugInData.find('Data').text,
					print PlugInData.find('Stop').text,
			#if root.find('Profile') is not None:
			#	print root.find('Profile').text
				
			"""---"""	
			#self.processdata(self.event_values)
			print
			
	def loadvixprofile(self,vixprofilename):
		if self.basedirpath != '':
			print "Using base dir path %s" % self.basedirpath
			checkfilepath = self.basedirpath + '/' + self.defaultprodir + vixprofilename + '.pro'
		else:
			print 'base file path not set'
			checkfilepath = vixprofilename
		print "loading profile file %s" % checkfilepath
		if not os.path.exists(checkfilepath):
			print ("Profile file '%s' not found" % checkfilepath)
		else:
			tree = ET.parse(checkfilepath)
			root = tree.getroot()
			print root.tag
			channel_objects = int(len(root.find('ChannelObjects')))
			print channel_objects
			if channel_objects > 0:
				self.channels = len(root.find('ChannelObjects'))
				print "setting channels from profile"
			if root.find('PlugInData') is not None:
				PlugInData = root.find('PlugInData')[0]
				#print PlugInData.get('name')
				#print PlugInData.get('enabled')
				#print PlugInData.get('from')
				#print PlugInData.get('to')
				if PlugInData.get('name') == 'Generic serial':
					pass
					#print PlugInData.find('Name').text
					#print PlugInData.find('Baud').text
					#print PlugInData.find('Parity').text
					#print PlugInData.find('Data').text
					#print PlugInData.find('Stop').text	

	def loadvixprogram(self,vixprogramname):
		if self.basedirpath != '':
			print "Using base dir path %s" % self.basedirpath
			checkfilepath = self.basedirpath + '/' + self.defaultprodir + vixprogramname
		else:
			print 'base file path not set'
			checkfilepath = vixprogramname
		print "loading profile file %s" % checkfilepath
		if not os.path.exists(checkfilepath):
			print ("Profile file '%s' not found" % checkfilepath)
		else:
			tree = ET.parse(checkfilepath)
			root = tree.getroot()
			print root.tag
			sequences = int(len(root.find('Sequence')))
			print sequences
			if sequences > 0:
				print "setting channels from profile"
			if root.find('Profile') is not None:
				tempprofilename = root.find('Profile').text
				print "attempting to load profile"
				self.loadvixprofile(tempprofilename)
					
	def basedir(self,dirname):
		self.basedirpath = dirname
		if not os.path.exists(self.basedirpath):
			raise BaseException("Path %s cannot be found" % self.basedirpath)
		
	
	def loadmusic(self,musicfilename):
		if self.basedirpath != '':
			checkfilepath = self.basedirpath + '/' + self.defaultmusdir + musicfilename
		else:
			checkfilepath = musicfilename
		print "loading file %s" % checkfilepath
		if os.path.exists(checkfilepath):
			self.has_musicfile = True
			self.musicfilename = checkfilepath		
			#print 'music loaded'
			print 'loading from loadmusic %s' % self.musicfilename
			pygame.mixer.init()
			pygame.mixer.music.load(self.musicfilename)
		else:
			self.musicfilename = ''
			print 'file %s not found' % musicfilename
		
	def play(self):
		self.ticks_init = pygame.time.get_ticks()

		if self.has_musicfile:
			pygame.mixer.music.play(0)
		else:
			print "music file not found, using ticks"
			self.ticks_init = pygame.time.get_ticks()
	
	def get_pos(self):
		if self.has_musicfile == True and pygame.mixer.music.get_pos() != -1: #self.musicfilename != '':
			#print "music_pos",
			return pygame.mixer.music.get_pos()
		else:
			ticks = pygame.time.get_ticks() - self.ticks_init
			#print "get_ticks" , ticks, "init", self.ticks_init
			return ticks
	
	def pos_syncwait(self,period,offset=0):
		x=0
		#print "get_pos", self.get_pos(), "ticks at per", self.ticks_at_per(int(period)), "period", period
		while self.get_pos() > 1 and self.get_pos() < self.ticks_at_per(int(period)) + offset:
			pass
			
	def channel(self):
		pass
	
	def ticks_at_per(self,period):
		return int((period) * int(self.permillis))
	
	def value(self,channel,period):
		return ord(self.sequence[channel][period])
		
	def set_value(self,channel,period,setval):
		#print self.value(channel,period)
		#print ord(self.sequence[channel][period]) == self.value(channel,period),
		#print "setting", ord(self.sequence[channel][period]), " to ", str(val)
		#self.sequence[channel][period] = hex(val)
		print type(self.sequence)
		print type(self.sequence[channel])
		print type(self.sequence[channel][period])
		print len(self.sequence[channel]) 
		#sequence is type list[str], a single value is the pos of char in str
		#set the channel string to a list so we can manipulate, then change back to string with join.
		temp = list(self.sequence[channel])
		temp[period] = chr(setval)
		self.sequence[channel] = "".join(temp)
		#self.sequence = seq
	
	def period_str(self,period):
		ret = "per: " + str('{:d}'.format(period)) + "/" + str('{:d}'.format(self.periods)) + ": " + ",".join(['{:03d}'.format(ord(self.sequence[x][period])) for x in range(self.channels)])
		return ret
		#'{:5d}'.format(period), 

	def period_arr(self,period):
		ret = [ord(self.sequence[x][period]) for x in range(self.channels)]
		return ret
		
	def processdata(self,datastr,channels=0):
		self.data = datastr.decode('base64')
		if channels > 0:
			self.channels = channels
		if self.channels == 0:
			raise BaseException("Channels = 0")
		self.periods = len(self.data)/self.channels
		#print "%s channels, %s periods" % (str(self.channels),str(self.periods))
		self.sequence = [ self.data[start:start+self.periods] for start in range(0, len(self.data), self.periods) ]
		#print str(self.sequence[0][0])
		#print "hello:" + str(hex(ord(self.sequence[0][0])))		
		
"""****************************************   TESTING   ****************************************"""
if __name__ == "__main__":		
	print "all testing moved to unit-test directory"
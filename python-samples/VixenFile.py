#VixenFile.py
#Parses VixenFiles
import os
import xml
import xml.etree.ElementTree as ET


class VixenFile(object):

	vixdirpath = ''
	seqdirpath = ''
	prodirpath = ''
	musdirpath = ''

	vixfilepath = ''
	seqfilepath = ''
	profilepath = ''
	musfilepath = ''

	vixdirname = ''
	seqdirname = ''
	prodirname = ''
	musdirname = ''

	seqfile = None
	profile = None
	musfile = None

	seqfilename = ''
	profilename = ''
	musfilename = ''
	
	seqxml = None
	proxml = None
	
	duration = 0
	title = 0
	
	def __init__(self,filename=None,dirname=None):
		self.
		self.openVixenFile(filename,dirname)
		
	def setdirpaths(self,dirname="VixenFiles"):
		self.vixdirpath = dirname
		self.seqdirpath = dirname + "/" + "Sequences"
		self.prodirpath = dirname + "/" + "Profiles"
		self.musdirpath = dirname + "/" + "Audio"
	
	def setprofilepath(self,ftype,filename):
		#check path, if not found, use vixenpath
		pass
	
	def openVixenFile(self,filename,dirname=None):
		
		if not os.path.exists(self.seqfilepath):
			raise Exception("File %s cannot be found" % self.seqfilepath)
		
	
	def parseSeqXML(self):
		if not os.path.exists(self.seqfilepath):
			raise "File %s cannot be found" % self.seqfilepath
		else:
			print "File %s found" % self.seqfilepath
			tree = ET.parse(self.seqfilepath)
			self.seqxml = tree.getroot()
			root = self.seqxml
			print root.tag
			print root.find('Time').text
			self.permillis = root.find('EventPeriodInMilliseconds').text
			if self.channels == 0:
				self.channels = len(root.find('Channels'))
			self.event_values = root.find('EventValues').text
			if root.find('Audio') is not None:
				self.musfilename = root.find('Audio').get('filename')
				self.duration = root.find('Audio').get('duration')
				self.title = root.find('Audio').text
			if root.find('PlugInData') is not None:
				pass
				PlugInData = root.find('PlugInData')[0]
				print PlugInData.get('name')
				print PlugInData.get('enabled')
				print PlugInData.get('from')
				print PlugInData.get('to')
				if PlugInData.get('name') == 'Generic serial':
					pass
					print PlugInData.find('Name').text
					print PlugInData.find('Baud').text
					print PlugInData.find('Parity').text
					print PlugInData.find('Data').text
					print PlugInData.find('Stop').text
			if root.find('Profile') is not None:
				print root.find('Profile').text
				
			"""---"""	
			#self.processdata(self.event_values)
		"""--- end parseSeqXML ---"""	
		
	def parseProXML(self):
		pass
		"""--- end parseProXML ---"""	
	
	def loadvixprofile(self,vixprofilename):
		profilefile = readfile(vixprofilename)
		if not profilefile:
			raise "Vixen profile file '%s' not found" % vixprofilename
		#profilefile = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\profiles\\" + root.find('Profile').text + ".pro"
		print profilefile
		if os.path.exists(profilefile):
			tree = ET.parse(profilefile)
			root = tree.getroot()
			print root.tag
			channel_objects = int(len(root.find('ChannelObjects')))
			print channel_objects
			if self.channels == 0 and channel_objects > 0:
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
	
	def loadmusic(self,musicfilename):
		if os.path.exists(musicfilename):
			self.has_musicfile = True
			self.musicfilename = musicfilename		
			#print 'music loaded'
			print 'loading from loadmusic %s' % self.musicfilename
			pygame.mixer.init()
			pygame.mixer.music.load(self.musicfilename)
		else:
			self.musicfilename = ''
			print 'file %s not found' % musicfilename

			
if __name__ == "__main__":		
	print "testing"
	vf = VixenFile("Test.vix")
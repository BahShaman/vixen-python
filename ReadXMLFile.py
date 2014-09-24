import os
import xml.etree.ElementTree as ET


#vixfilename = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Sequences\\PythonDecodeSample2.vix"
vixfilename = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Sequences\\Arduino6ChannelThisIsHolloweenMain.vix"
if os.path.exists(vixfilename):
	tree = ET.parse(vixfilename)
	root = tree.getroot()
	print root.tag
	print root.find('Time').text
	print root.find('EventPeriodInMilliseconds').text
	print len(root.find('Channels'))
	data  = root.find('EventValues').text
	if root.find('Audio') is not None:
		print root.find('Audio').get('filename')
		print root.find('Audio').get('duration')
		print root.find('Audio').text
	if root.find('PlugInData') is not None:
		PlugInData = root.find('PlugInData')[0]
		print PlugInData.get('name')
		print PlugInData.get('enabled')
		print PlugInData.get('from')
		print PlugInData.get('to')
		if PlugInData.get('name') == 'Generic serial':
			print PlugInData.find('Name').text
			print PlugInData.find('Baud').text
			print PlugInData.find('Parity').text
			print PlugInData.find('Data').text
			print PlugInData.find('Stop').text
	if root.find('Profile') is not None:
		print root.find('Profile').text
		profilefile = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\profiles\\" + root.find('Profile').text + ".pro"
		print profilefile
if os.path.exists(profilefile):
	tree = ET.parse(profilefile)
	root = tree.getroot()
	print root.tag
	print len(root.find('ChannelObjects'))
	if root.find('PlugInData') is not None:
		PlugInData = root.find('PlugInData')[0]
		print PlugInData.get('name')
		print PlugInData.get('enabled')
		print PlugInData.get('from')
		print PlugInData.get('to')
		if PlugInData.get('name') == 'Generic serial':
			print PlugInData.find('Name').text
			print PlugInData.find('Baud').text
			print PlugInData.find('Parity').text
			print PlugInData.find('Data').text
			print PlugInData.find('Stop').text
	


	
			
	
	

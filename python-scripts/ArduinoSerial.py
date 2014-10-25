import serial
import serial.tools.list_ports
import time

class ArduinoSerial(object):

	sendbytes = []
	wport = None

	def __init__(self,wport="Auto"):
		self.port(wport)
		
	def __del__(self):
		try:
			self.wport.close()
		except:
			pass

	def test(self,length=8):
		for x in range(length):
			time.sleep(.1)
			data = []
			for i in range(length):
				if x == i:
				#if x % 1 == i % 1:
					my_int = 255
				else:
					my_int = 0
				data.append(my_int)
				print " {:3d}".format(my_int) , 
			Ard.send(data)
			print "ArduinoSerial Test, length: %s" % len(data)

	def port(self,port="Auto"):
		#try:
		aport = []
		if port=="Auto":
			aport = self.autoport()
			if aport:
				self.wport = serial.Serial(aport[0], baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3.0)
				print "Using",
				print aport
		else:
			self.wport = serial.Serial(port, baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3.0)
			#self.wport = serial.Serial('/dev/ttyUSB0', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3.0)
		#except serial.SerialException:
		#	self.wport = None
		#except:
		#	self.wport = None
	
	def autoport(self):
		ports = list(serial.tools.list_ports.comports())
		print "%d ports found" % len(ports)
		'''note this only returns the first port'''
		for port in ports:
			print "\t",
			print port
			return port
			
	
	def sendbytes(self,bytearray):
		if self.wport:
			self.wport.write(bytearray)
			return bytearray
		else:
			return False

	def send(self,intarray):
		bytearray = []
		for x in intarray:
			bytearray.append(bytes(chr(x)),)
		self.sendbytes(bytearray)
		return bytearray
		
"""****************************************   TESTING   ****************************************"""
if __name__ == "__main__":		
	Ard = ArduinoSerial("COM4")
	Ard.test()
	for z in range(1):
		for x in range(8):
			time.sleep(.1)
			data = []
			for i in range(8):
				if x == i:
				#if x % 1 == i % 1:
					my_int = 255
				else:
					my_int = 0
				data.append(my_int)
				print " {:3d}".format(my_int) ,
			Ard.send(data)
			print len(data)
	Ard.send([0,0,0,0,0,0,0,0])
	
	"""testing Auto"""
	Ard = None	

	print "failing..."
	try:
		Ard = ArduinoSerial("Bogus")
		Ard.test()
	except:
		print "PASS"
	
	Ard = None	
	Ard = ArduinoSerial()
	Ard.test()
	Ard.send([255,0,255,0,255,0,255,0])
	for z in range(4):
		for x in range(8):
			time.sleep(.1)
			data = []
			for i in range(8):
				#if x == i:
				if x % 3 == i % 3:
					my_int = 255
				else:
					my_int = 0
				data.append(my_int)
				print " {:3d}".format(my_int) ,
			Ard.send(data)
			print len(data)
	print Ard.send([0,0,0,0,0,0,0,0])
	print Ard.send([0,0,0,0,0,0,0,0])

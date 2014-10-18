import serial
import serial.tools.list_ports
import time

class ArduinoSerial(object):

	sendbytes = []
	wport = None

	def __init__(self,wport="Auto"):
		self.port(wport)

	def test(self,length=8):
		for x in range(length):
			self.send([255,0,255,0,255,0,255,0])
			time.sleep(.5)

	def port(self,wport="Auto"):
		try:
			self.wport = serial.Serial('COM4', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3.0)
		except serial.SerialException:
			self.wport = None

		
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
	print Ard.send([255,0,255,0,255,0,255,0])
	while True:
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

	
	
	
	
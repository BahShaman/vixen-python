#python serial output
import serial
import serial.tools.list_ports
import time

"""
i=0
try:
	ser = serial.Serial(None, 9600, timeout=1)
	ser.close()
	ser.open()
	ser.write("ati")
	ser.read(64)
except serial.SerialException:
	pass
i+=1
"""

"""
try:
	port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
except serial.SerialException:
	print "hello"
"""

	
ports = list(serial.tools.list_ports.comports())
print "%d ports found" % len(ports)
for port in ports:
	print port
	useport = port
	break

	
print serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE
"""
if False:	
	#try:
	wport = serial.Serial('COM4', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3.0)
	#wport.open()
	print wport
	wport.write("hello")
	print "starting"
	st = ""
	while True:
		#print "printing %s" % 0
		for x in range(8):
			time.sleep(2)
			for i in range(8):
				if x % 3 == i % 3:
					my_int = 255
				else:
					my_int = 0
				st += str(" {:d}".format(i % 3)) + "=" + str("{:d}".format(x % 3))
				print " {:3d}".format(my_int) ,
				print len(bytes(chr(my_int)))
				wport.write(bytes(chr(my_int)))
			wport.write(chr(13))
			#print wport.readline()
			print st
			st = ""
			x = raw_input("pausing")
	while True:
		print wport.read(1),
	#except serial.SerialException:
	#	print "error reading from port %s" % wport.name
"""		


if True:	
	#try:
	wport = serial.Serial('COM4', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3.0)
	print wport
	print "starting"
	while True:
		for x in range(8):
			#time.sleep(2)
			sendbytes = []
			for i in range(8):
				if x == i:
				#if x % 1 == i % 1:
					my_int = 255
				else:
					my_int = 0
				sendbytes.append(bytes(chr(my_int)),)
				#sendbytes.append("!")
				print " {:3d}".format(my_int) ,
				#print len(bytes(chr(my_int)),) ,
			wport.write(sendbytes)
			print len(sendbytes)
			#print "[" ,
			#print sendbytes ,
			#print "]" ,
			z = raw_input("pausing")
	while True:
		print wport.read(1),
	#except serial.SerialException:
	#	print "error reading from port %s" % wport.name



"""
#try:
wport = serial.Serial('COM4', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3.0)
#wport.open()
print wport
wport.write("hello")
print "starting"
st = ""
while True:
	#print "printing %s" % 0
	for x in range(8):
		time.sleep(2)
		for i in range(8):
			if x % 3 == i % 3:
				my_int = 255
			else:
				my_int = 0
			st += str(" {:d}".format(i % 3)) + "=" + str("{:d}".format(x % 3))
			print " {:3d}".format(my_int) ,
			print len(bytes(chr(my_int)))
			wport.write(bytes(chr(my_int)))
		wport.write(chr(13))
		#print wport.readline()
		print st
		st = ""
		x = raw_input("pausing")
while True:
	print wport.read(1),
#except serial.SerialException:
#	print "error reading from port %s" % wport.name
"""		
		
		
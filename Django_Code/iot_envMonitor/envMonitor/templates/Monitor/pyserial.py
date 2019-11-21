import serial
try:
	arduino=serial.Serial("/dev/ttyUSB0",timeout=7,baudrate=115200)
except:
	print "hello"
count=0
print arduino
arduino.flush() 
while count < 10:
	count+=1
	print str(arduino.read(25000))
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
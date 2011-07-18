import time, serial

try:
	ser = serial.Serial('/dev/ttyUSB0', 9600)

	while True:
		if ser.readline() == 'SYN':
			ser.write('ACK')
		else:
			time.sleep(1)

except serial.SerialException, e:
	print e
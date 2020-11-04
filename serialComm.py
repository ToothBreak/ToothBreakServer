from serial import Serial
serialPort = "/dev/ttyACM0"
ser = Serial(serialPort, 9600)

def serialWrite(msg):
    ser.write(msg)

def serialClose():
    ser.close()
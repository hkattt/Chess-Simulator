import serial

s = serial.Serial('COM6', 9600)
print("")
print(s)
print("")
s.write(b'hello')
s.close()

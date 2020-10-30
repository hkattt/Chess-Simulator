import serial

s = serial.Serial('COM7', 9600)
print("")
print(s)
print("")

s.write(b"1111")
#msg = s.readline()
#print(msg)
s.close()

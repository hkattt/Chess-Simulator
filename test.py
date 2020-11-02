import serial
import time

s = serial.Serial('COM8', 9600)
print("")
print(s)
print("")

while True:
    s.write(b"1")
    time.sleep(1)
msg = s.readline()
print(msg)
s.close()

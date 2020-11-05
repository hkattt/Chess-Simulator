import serial
import time

# NOTE: When sending data comment out the receiving data part and vice-versa

# creates serial object
# PORT: COM7
# Baud rate: 9600
s = serial.Serial('COM7', 9600)
print("")
print(s)
print("")

# sends data
time.sleep(3)
s.write(b"012")
time.sleep(3)

# receives data
msg = s.readline()
print(msg)
print("")

# closes the serial port
s.close()
print("CLOSED")




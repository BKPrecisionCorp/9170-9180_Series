import math
import serial

comNum = input("COMM port number?")
ser = serial.Serial()
ser.baudrate = 57600
ser.port = 'COM'+comNum
ser.timeout = 1
ser.open()
open = ser.is_open
ser.flush

ser.write("*idn?\n".encode())
print(ser.readline())

ser.write("prog 1\n".encode())
ser.write("prog:cle\n".encode())
ser.write("prog:rep 0\n".encode())
ser.write("prog:total 100\n".encode())

for i in range(150):
    ser.write(("prog:step " + str(i) + "\n").encode())
    x = math.fabs(0.25*math.exp(i/110)*math.sin(i/(5*3.141)))
    print(float("{0:.3f}".format(x)))
    ser.write(("prog:step:curr "+str(float("{0:.3f}".format(x)))+"\n").encode())
    ser.write("prog:step:volt 5\n".encode())
    ser.write("prog:step:ont 0.01\n".encode())

ser.write("prog:next 0\n".encode())
ser.write("prog:save\n".encode())


import serial
import time

ser = serial.Serial("com9")
ser.baudrate = 57600
print(ser.name)
ser.write(b'*idn?\r\n')
print(ser.readline())
ser.write(b'prog 1\r\n')
ser.write(b'prog:rep 0\r\n')
ser.write(b'prog:tota 1\r\n')

ser.write(b'prog:step 1\r\n')
ser.write(b'prog:curr 1\r\n')
ser.write(b'prog:volt 1\r\n')
ser.write(b'prog:ont 0.1\r\n')


#for i in range(1):
#    cmd = 'prog:step '+str(i+1)+'\r\n'
#    print(cmd)
#    ser.write(cmd.encode())
#    ser.write(b'prog:step:curr 1\r\n')
#    cmd = 'prog:step:volt '+str(2*i)+'\r\n'
#    print(cmd)
#    ser.write(cmd.encode())
#    ser.write(b'prog:step:ont 0.1\r\n')
        
ser.write(b'prog:next 0\r\n')
ser.write(b'prog:sav\r\n')

ser.close()



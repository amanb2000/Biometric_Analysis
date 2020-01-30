#!/usr/bin/python
import serial
import syslog
import time
import sys



#The following line is for serial over GPIO
port = '/dev/cu.usbmodem144301'


ard = serial.Serial(port,9600,timeout=5)

i = 0

running = True

r_ind = 0
# Exercise-part-person
# Person 1: 
# Person 2: 
# Person 3:
# Person 4: 
path = 'data/'
path += sys.argv[1]
path += '.csv'

f= open(path,"w+")

f.write('eda,\n')

while running:  
    # Serial write section
    time.sleep(0.01) # with the port open, the response will be buffered 
                  # so wait a bit longer for response here

    # Serial read section
    msg = ard.read(ard.inWaiting()) # read everything in the input buffer
    # print ("Message from arduino: ")
    # print (msg[0]])
    

    int_msg = -1

    try:
        str_msg = msg.decode("utf-8")
        r_ind = str_msg.index('\r')
        int_msg = int(str_msg[:r_ind])
    except:
        int_msg = -1 
    
    if int_msg == -1:
        try:
            int_msg = int(msg)
        except:
            int_msg = -1

    if(int_msg != -1):
        print(int_msg)
        f.write(str(int_msg)+',\n')
    # print(msg.decode("utf-8"))
    # for m in msg:
        # print(m)
        # print(int.from_bytes(m, byteorder='big'))

exit()

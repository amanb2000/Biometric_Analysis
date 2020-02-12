#!/usr/bin/python
import serial
import syslog
import time
import sys



#The following line is for serial over GPIO
port = '/dev/cu.usbmodem144401'


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
    
    # print(msg)
    arry_msg = []

    try:
        str_msg = msg.decode("utf-8")
        arry_msg = str_msg.split('\r')
    except:
        int_msg = -1 
    
    for int_msg in arry_msg:
        if int_msg == -1:
            try:
                int_msg = int(msg)
            except:
                int_msg = -1

        if(int_msg != -1 and int_msg.strip() != ''):
            print(int_msg) 
            f.write(str(int_msg)+',\n')
    # print(msg.decode("utf-8"))
    # for m in msg:
        # print(m)
        # print(int.from_bytes(m, byteorder='big'))

exit()

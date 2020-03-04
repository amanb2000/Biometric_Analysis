#!/usr/bin/python
import serial
import syslog
import time
import sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from matplotlib import style

import live_plot

style.use('fivethirtyeight')



class Data_Logger:
    def __init__(self):
        """
        Takes in the name of the file you want to write to.
        """
        try:
            config_dict = {}
            with open('config.json') as f:
                    config_dict = json.load(f)
            self.port = config_dict['board_address']
        except:
            raise('ERR: Invalid config.json file. Make sure it exists and follows the format specified in the repository.')
        finally:
            print('\nconfig.json is valid and was read from.\n')

        try:
            self.ard = serial.Serial(self.port,9600,timeout=5)
        except:
            raise('ERR: The specified serial port could not be connected to. Double check the number and confirm that you have the correct format and connectivity.')
        finally:
            print('\nSuccessfully connected to arduino port...\n')
            

    def collect_data(self, f_name, num_seconds, make_plot=True):
        """Takes in data from the arduino and writes it to a file name dictated by the user (in the data folder)"""

        self.fname = f_name

        path = 'data/'
        path += f_name
        path += '.csv'

        running = True
        
        begin_time = time.time()
        cur_time = begin_time

        f = open(path, "w")

        f.write('time,data')

        print('\n\nCollecting and writing data to data/{}.csv for {} seconds\n\n'.format(f_name, num_seconds))

        # live_plot.plot(f_name)

        while cur_time-begin_time < num_seconds:  
            cur_time = time.time()           
 
            time.sleep(0.001) # with the port open, the response will be buffered 
                              # so wait a bit longer for response here

            msg = self.ard.read(self.ard.inWaiting()) # read everything in the input buffer
            
            arry_msg = []

            try:
                str_msg = msg.decode("utf-8")
                arry_msg = str_msg.split('\r')
            except:
                arry_msg = [''] 
            
            for int_msg in arry_msg: # iterating through the split input string buffer
                if int_msg == -1:
                    try:
                        int_msg = int(msg)
                    except:
                        int_msg = -1

                if(int_msg.strip() != -1 and int_msg.strip() != ''):
                    print(int_msg)
                    f.write('\n'+str(cur_time-begin_time)+','+str(int_msg))

        print('\n\nProcess done. File saved to {}\n\n'.format(f_name))


    def plot_file(self, file_name, title='BME_LAB', xname='Time (s)', yname='Amplitude'):
        """Takes in file name and plots the data that's located in `data/file_name`"""

        path = 'data/'
        path += file_name
        path += '.csv'

        df = pd.read_csv(path)
            

        df = df[df['data'] > 0]
        df = df[df['data'].notnull()]

        print(df.columns)
        plt.plot(df['time'], df['data'])

        plt.show()



if __name__ == '__main__':
    data_logger = Data_Logger()
    data_logger.collect_data('rate', 10)
    data_logger.plot_file('rate')









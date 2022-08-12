#this program will take a matlab frequency plot in CSV format and convert it into a wav file

import argparse
import csv
import math
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import pandas as pd

sample_rate = 44100
start_time = 0
end_time = 10
theta = 0

#create the argument parser
parser = argparse.ArgumentParser(description='Convert a frequency plot file to a wav file')
#add the arguments
parser.add_argument('--file', '-f', help='The file to convert', required=True)
parser.add_argument('--output', '-o', help='The output file', required=True)
#parse the arguments
args = parser.parse_args()
#print the file name of the source frequency plot to be converted and the output file name
print('Converting ' + args.file + ' to ' + args.output)

# open the file to convert and read the data into a dataframe using pandas 
# the first column is the frequency and the second column is the amplitude
# The file is not expecting a header row and the file location defaults to the current directory
df = pd.read_csv(args.file, header=None, names=['frequency', 'amplitude'])

# create an audio file from the frequency plot and save it to the output file
# the sampling rate is sample_rate var in Hz

# create an array of zeros to hold the audio data for the sample_rate
audio = np.zeros(sample_rate)

# create an array of sample_rate evenly spaced numbers from 0 to sample_rate multiplied by the end_time
# this is the time axis
timedomain = np.linspace(start_time, end_time, end_time * sample_rate)
#timedomain = np.linspace(start_time, end_time, sample_rate)
sinewave = np.empty(len(timedomain))
# create a continuous sine wave for each row in the dataframe of length sample_rate samples
# the frequency is the frequency in the dataframe
# the amplitude is the amplitude in the dataframe
# the phase is 0 (defined above)
# the time axis is the timedomain array

# combine all of the sine waves into a single audio file
for index, row in df.iterrows():
    # combine all the sinewaves into a single sinewave
    # create a random value for theta that is between negative pi and pi
    theta = np.random.uniform(-math.pi, math.pi)
    sinewave += row['amplitude'] * np.sin(2 * np.pi * row['frequency'] * timedomain + theta)
    # save each sine wave to its own wav file with the frequency as the file name
    # wav.write(str(row['frequency']) + '.wav', sample_rate, audio) #debug

# save the combined sinewaves to the output file
wav.write(args.output, sample_rate, sinewave)

# show the frequency plot in a matplotlib window
#plt.plot(df['frequency'], df['amplitude'])
#plt.show()

# show the resulting audio file in a matplotlib window
plt.plot(timedomain, sinewave)
plt.show()
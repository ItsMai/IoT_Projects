# Mailani Gelles / Emily Kuo 
# github.com/usc-ee250-fall2019/lab08-emily-mailani
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import os
import sys

MAX_FRQ = 2000
SLICE_SIZE = 0.15 #seconds
WINDOW_SIZE = 0.25 #seconds
NUMBER_DIC = {}

# LOWER_FRQS = [697, 770, 852, 941]
# HIGHER_FRQS = [1209, 1336, 1477, 1633]
FRQ_THRES = 20

def get_max_frq(frq, fft):
    max_frq = 0
    max_fft = 0
    for idx in range(len(fft)):
        if abs(fft[idx]) > max_fft:
            max_fft = abs(fft[idx]) 
            max_frq = frq[idx]
            # print(abs(fft[idx]), max_fft, frq[idx], max_frq)
    return max_frq

def get_peak_frqs(frq, fft):
    #TODO: implement an algorithm to find the two maximum values in a given array
    low_frq_fft = fft[:int(len(fft)/2)]
    high_frq_fft = fft[int(len(fft)/2):]
    low_frq = frq[:int(len(fft)/2)]
    high_frq = frq[int(len(fft)/2):]
    #get the high and low frequency by splitting it in the middle (1000Hz)

    #spliting the FFT to high and low frequencies

    return (get_max_frq(low_frq, low_frq_fft), get_max_frq(high_frq, high_frq_fft))

def get_number_from_frq(lower_frq, higher_frq):
    #TODO: given a lower frequency and higher frequency pair
    #      return the corresponding key otherwise return '?' if no match is found
    if 680 <= lower_frq <= 720  :
        if 1190 <= higher_frq <= 1220:
            return '1'
        elif 1300<= higher_frq <= 1350:
            return '2'
        elif 1450 <= higher_frq <= 1500:
            return '3'
        else:
            return '?'
    elif 750 <= lower_frq <= 790:
        if 1190 <= higher_frq <= 1220:
            return '4'
        elif 1300<= higher_frq <= 1350:
            return '5'
        elif 1450 <= higher_frq <= 1500:
            return '6'
        else:
            return '?'
    elif 830 <= lower_frq <= 870:
        if 1190 <= higher_frq <= 1220:
            return '7'
        elif 1300<= higher_frq <= 1350:
            return '8'
        elif 1450 <= higher_frq <= 1500:
            return '9'
        else:
            return '?'
    elif 920 <= lower_frq <= 960:
        if 1190 <= higher_frq <= 220:
            return '*'
        elif 1300<= higher_frq <= 1350:
            return '0'
        elif 1450 <= higher_frq <= 1500:
            return '#'
        else:
            return '?'
    else:
        return '?'

def main(file):
    print("Importing {}".format(file))
    audio = AudioSegment.from_mp3(file)

    sample_count = audio.frame_count()
    sample_rate = audio.frame_rate
    samples = audio.get_array_of_samples()

    print("Number of channels: " + str(audio.channels))
    print("Sample count: " + str(sample_count))
    print("Sample rate: " + str(sample_rate))
    print("Sample width: " + str(audio.sample_width))

    period = 1/sample_rate                     #the period of each sample
    duration = sample_count/sample_rate         #length of full audio in seconds

    slice_sample_size = int(SLICE_SIZE*sample_rate)   #get the number of elements expected for [SLICE_SIZE] seconds
    time = np.arange(0, duration, period)   #generate a array of time values from 0 to [duration] with step of [period]

    n = slice_sample_size                            #n is the number of elements in the slice

    #generating the frequency spectrum
    k = np.arange(n)                                #k is an array from 0 to [n] with a step of 1
    slice_duration = n/sample_rate                   #slice_duration is the length of time the sample slice is (seconds)
    frq = k/slice_duration                          #generate the frequencies by dividing every element of k by slice_duration

    max_frq_idx = int(MAX_FRQ*slice_duration)       #get the index of the maximum frequency (2000)
    frq = frq[range(max_frq_idx)]                   #truncate the frequency array so it goes from 0 to 2000 Hz

    start_index = 0                                 #set the starting index at 0
    end_index = start_index + slice_sample_size      #find the ending index for the slice
    output = ''

    print()
    i = 1
    while end_index < len(samples):
        print("Sample {}:".format(i))
        i += 1                     
        #generate the frequencies by dividing every element of k by slice_duration
        sample_slice = samples[start_index: end_index]  #take a slice from the samples array for the given start and end index
        
        #TODO: truncate the FFT to 0 to 2000 Hz
        sample_slice_fft = np.fft.fft(sample_slice)/n   #perform the fourier transform on the sample_slice and normalize by dividing by n
        sample_slice_fft = sample_slice_fft[range(max_frq_idx)]     #truncate the sample slice fft array so it goes from 0 to 2000 Hz

        #TODO: calculate the locations of the upper and lower FFT peak using get_peak_frqs()
        (lo, hi) = get_peak_frqs(frq, sample_slice_fft)

        #TODO: print the values and find the number that corresponds to the numbers
        print (get_number_from_frq(lo, hi))

        #Incrementing the start and end window for FFT analysis
        start_index += int(WINDOW_SIZE*sample_rate)
        end_index = start_index + slice_sample_size

    print("Program completed")
    print("User typed: " + str(output))

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print("Usage: decode.py [file]")
        exit(1)
    main(sys.argv[1])

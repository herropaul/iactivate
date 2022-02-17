#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 00:51:49 2020

@author: calvin
"""

import pandas as pd
import matplotlib.pyplot as plt
import pickle
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

df = pd.read_csv('BVP_Signals.csv')
df = df.T
df = df.iloc[:,0:6400]
patient1 = df.iloc[0,:]
'''
patient2 = df.iloc[1,:]
patient3 = df.iloc[2,:]
patient4 = df.iloc[3,:]
patient5 = df.iloc[4,:]
patient6 = df.iloc[5,:]
patient7 = df.iloc[6,:]
patient8 = df.iloc[7,:]
patient9 = df.iloc[8,:]
patient10 = df.iloc[9,:]
patient11 = df.iloc[10,:]
patient12 = df.iloc[11,:]
'''


#plt.figure()
#plt.plot(patient1)


plt.title('Patient 1: BPV Signal')
plt.xlabel('60 second window')
plt.xlim(0,383)

plt.axvline(x=63, color = 'orange')
plt.axvline(x=2*63, color = 'orange')
plt.axvline(x=63, color = 'orange')
plt.axvline(x=3*63, color = 'orange')
plt.axvline(x=63, color = 'orange')
plt.axvline(x=4*63, color = 'orange')
plt.axvline(x=63, color = 'orange')
plt.axvline(x=5*63, color = 'orange')
plt.axvline(x=63, color = 'orange')
plt.axvline(x=6*63, color = 'orange')
'''
plt.figure()
plt.plot(patient2)
plt.figure()
plt.plot(patient3)
plt.figure()
plt.plot(patient4)
plt.figure()
plt.plot(patient5)
plt.figure()
plt.plot(patient6)
plt.figure()
plt.plot(patient7)
plt.figure()
plt.plot(patient8)
plt.figure()
plt.plot(patient9)
plt.figure()
plt.plot(patient10)
plt.figure()
plt.plot(patient11)
plt.figure()
plt.plot(patient12)
'''

#Global Definitions
#this is the amount of data points in every second
SamplesPerSecond = 64
#the mount of samples per second in our sample time window
Timewindow = 15
sBPM = 1 * 60
#Static Calculations in global definitions
TotalSamplesPerWindow = SamplesPerSecond * Timewindow
WindowsPerBPM = sBPM / Timewindow
#End of Global Definitions

#NAnother Function
#AvgBPM = WindowsPerMinute * ResultOfBPTPeaks


BigData = patient1.tolist()
CompiledBPM = []
#main()

def BPTPeaks(data, s_rate, window):
    peaks = []
    peakCount = 0
    i = 1
    #lastPeakValue =
    while i < len(data) - 1:
        if(data[i - 1] < data[i] and data[i] > data[i+1]):
            peaks.append(data[i])
        i = i + 1
    return peaksInSet

def main():
    TotalSegments = len(BigData) / TotalSamplesPerWindow
    TotalSampleSets = len(BigData) / SamplesPerSecond
    TotalSegmentsInSamples = TotalSegments / SamplesPerSecond
    LastPeakSeconds = NULL
    BPMCompiledTW = []
    i = 0
    CurrentSampleSegments = 0
    SampleWindowData = []
    TimeWindowDataPoints = []
    SecondsCount = 0
    while i < TotalSampleSets:
        #current_start_index = i * SamplesPerSegment
        #twIndex
        #while twIndex < TimeWindow
        #this is the data set of the current segment which is 64 data points.
        #SmallerSampleSetData = []
        #the current index of the segment of 64 data points we are cycling through
        i_of_set = 0
        while i_of_set < SamplesPerSecond:
            #cycle through the bigger data in groupings of 64 but add each data point of the segment to a time window data point array.
           #SmallerSampleSetData.append(BigData[(i * SamplesPerSecond) + (i_of_set = i_of_set + 1)])
           TimeWindowDataPoints.append(BigData[(i * SamplesPerSecond) + i_of_set])
           i_of_set = i_of_set + 1
        SecondsCount = SecondsCount + 1
        if SecondsCount == Timewindow:
            #Calculate BPM HERE add to bpm result table
            AVGBPTWProduct = NULL
            BPTWindowProduct = BPTPeaks(TimeWindowDataPoints, SamplesPerSecond, Timewindow)
            if LastPeakSeconds != NULL:
                AVGBPTWProduct = BPTWindowProduct + LastPeakSeconds / 2
            BPM = WindowsPerBPM * BPTWindowProduct
            CompiledBPM.append(BPM)
            LastPeakSeconds = BPTWindowProduct
            TimeWindowDataPoints = []
            SecondsCount = 0
        i = i + 1
    print("Done with main.")

main()
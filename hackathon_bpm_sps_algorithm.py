# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 00:28:04 2020

@author: herro
"""

import pickle
import pandas as pd
import csv 

import csv
#Global Definitions
#this is the amount of data points in every second
SamplesPerSecond = 64
#the mount of samples per second in our sample time window
Timewindow = 15
sBPM = 1 * 60
TotalSamplesPerWindow = SamplesPerSecond * Timewindow
WindowsPerBPM = sBPM / TimeWindow
#End of Global Definitions

#NAnother Function
#AvgBPM = WindowsPerMinute * ResultOfBPTPeaks


BigData = []
with open('C:\Users\herro\Desktop\Hackathon_Data\bvp_export_test.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        BigData.append(float(row[0]))

def main():
    TotalSegments = len(BigData) / TotalSamplesPerWindow
    TotalSampleSets = len(BigData) / SamplesPerSecond
    TotalSegmentsInSamples = TotalSegments / SamplesPerSecond
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
        SmallerSampleSetData = []
        #the current index of the segment of 64 data points we are cycling through
        i_of_set = 0
        while i_of_set < SamplesPerSecond:
            #cycle through the bigger data in groupings of 64 but add each data point of the segment to a time window data point array.
           SmallerSampleSetData.append(BigData[(i * SamplesPerSecond) + (i_of_set = i_of_set + 1)])
           TimeWindowDataPoints.append(BigData[(i * SamplesPerSecond) + (i_of_set = i_of_set + 1)])
    SecondsCount++
    if SecondCount == Timwwindow:
        #Calculate BPM HERE add to bpm result table
        BPTWindowProduct = BPTPeaks(TimeWindowDataset, SamplesPerSecond, Timewindow)
        BPM = WindowsPerBPM * BPTWindowProduct
        BPMCompiledTW.append(BPM)
        SecondCount = 0
        
           
       
           
        
        #billions
        #64 Samples
        #64 Data points = (1 second) * 15s TimeWindow  = 960 total data points per time window out of the Big Data Array
        #We need to offset and increment in 64 data point segments to remove one second of data andd a new second of data
        
        #TimeWindowDataSet = CycleThroughBigData(BigData, TotalSamplesPerWindow, i)
       
        #Display our BPM on a second graph to get BPM per second changes


#def DataWithOffest(bData, asize, offset)

def CycleTHroughBigData(bData, asize, TotalSegments, page = 0):
    i = TotalSegments * page
    length = (page * TotalSegments)
    newDataSet = []
    while i < length:
        newDataSet.append(bData[i++])
    return newDataSet
    
        

def BPTPeaks(data, s_rate, window):
    peaks = []
    for i in range(len(data)):
        if (data[i] > data[i+1]):
            peaks += 1
            peaks.append(i)
    wpm = 60 / window
    bpm = wpm * peaks
    return bpm

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
''' The total time of the song is 3 seconds starting from zero for 12*1024 samples'''
t = np.linspace(0 , 3 , 12*1024)

F3 = np.array([130.81,146.83,164.81,174.61,196,220,246.93])
F4 = np.array([261.63,293.66,329.63,349.23,392,440,493.88])
ti = np.array([0, 1.2, 1.4, 1.6, 2.5, 3.7, 3.9])
Ti = np.array([0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1])
n=7
Pi=np.pi
Song=0
for i in range(n):
    LeftHandFreq=F3[i]
    RightHandFreq=F4[i]
    DurationTime=Ti[i]
    StartingTime=ti[i]
    LeftHandNote=np.sin(2*Pi*LeftHandFreq*t)
    RightHandNote=np.sin(2*Pi*RightHandFreq*t)
    Song+=(LeftHandNote+RightHandNote)*((t>=StartingTime)&(t<=(StartingTime+DurationTime)))
    i+=1
plt.plot(t, Song)
sd.play(Song,3*1024)
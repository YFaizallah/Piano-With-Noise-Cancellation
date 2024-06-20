import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import math

t = np.linspace(0,3, 12*1024)

x1 = np.reshape((np.sin(2*np.pi*261.63*t)+np.sin(2*np.pi*130.81*t))*np.logical_and(t>=0, t< 0.4), np.shape(t))
x2 = np.reshape((np.sin(2*np.pi*261.63*t)+np.sin(2*np.pi*130.81*t))*np.logical_and(t>=0.45, t< 0.85), np.shape(t))
x3 = np.reshape((np.sin(2*np.pi*392*t)+np.sin(2*np.pi*196*t))*np.logical_and(t>= 0.9, t< 1.25), np.shape(t))
x4 = np.reshape((np.sin(2*np.pi*392*t)+np.sin(2*np.pi*196*t))*np.logical_and(t>=1.3, t< 1.7), np.shape(t))
x5 = np.reshape((np.sin(2*np.pi*440*t)+np.sin(2*np.pi*220*t))*np.logical_and(t>=1.8, t< 2.2), np.shape(t))
x6 = np.reshape((np.sin(2*np.pi*440*t)+np.sin(2*np.pi*220*t))*np.logical_and(t>=2.25, t<2.55), np.shape(t))
x7 = np.reshape((np.sin(2*np.pi*392*t)+np.sin(2*np.pi*196*t))*np.logical_and(t>=2.6, t< 3), np.shape(t))

x = x1 + x2 + x3 + x4 + x5 + x6 + x7

N = 3*1024
f = np. linspace(0 , 512 , int(N/2))

#Fourier Transform of Original Sound.
x_f = fft(x)
x_f = 2/N * np.abs(x_f [0: int(N/2)])

#Generating the Noise
fn1 , fn2 = np.random.randint(0, 512, 2)
n = np.sin(2*np.pi*fn1*t)+np.sin(2*np.pi*fn2*t)

#Adding the noise to the original Signal and transforming it into frequency domain.
xn = x + n
n_f = fft(xn)
n_f = 2/N * np.abs(n_f [0: int(N/2)])


#Filtering the noise from the signal (peaks is a tuple with w values that have higher peaks than x)
peaks = np.where(n_f > math.ceil(np.max(x)))
w1 = peaks[0][0]
w2 = peaks[0][1]

#Getting frequencies by getting the value at w = peaks.
# int typecast to avoid including maximum value due to double percision errors.
n1 = int(f[w1])
n2 = int(f[w2])

filteredSignal = xn - (np.sin(2*np.pi*n1*t)+np.sin(2*np.pi*n2*t))
filteredFT = fft(filteredSignal)
filteredFT =  2/N * np.abs(filteredFT [0: int(N/2)])


#Plots : 

plt.figure()    
plt.subplot(2,1,1)
plt.plot(t,x)
plt.title("Signal without noise in time domain")
plt.subplot(2,1,2)
plt.tight_layout()
plt.plot(t, xn)
plt.title("Signal with noise in time domain")

plt.figure()
plt.subplot(2,1,1)
plt.plot(f, x_f)
plt.title("Signal without noise in frequency domain")
plt.subplot(2,1,2)
plt.tight_layout()
plt.plot(f, n_f)
plt.title("Signal with noise in frequency domain")

plt.figure()
plt.subplot(2,1,1)
plt.plot(f, filteredFT)
plt.title("Signal after filtering noise in frequency domain")
plt.subplot(2,1,2)
plt.tight_layout()
plt.plot(t, filteredSignal)
plt.title("Signal after filtering noise in time domain")

#Playing the filtered sound: 
sd.play(filteredSignal, 4*1024)
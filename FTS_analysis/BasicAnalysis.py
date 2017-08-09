#Basic analysis (not including demodulation or deconvolution)
#Given a pickle file of an interferogram this plots the interferogram (using a power of 2 samples)
#it then plots the spectrum (the fourier transform of the interferogram). Mira

import numpy as np
import matplotlib
import matplotlib.pyplot as pl
import pickle
import sys
import numpy as np


filename = input('Enter file name: ')
with open('../Data/' +str(filename) , 'rb') as f:
    d = pickle.load(f, encoding='latin1') #delete 'encoding = latin1' if using python 2.x only needed for python3.x
    
i = 11
Nsize = 2**i
dt=(1/(d['sample freq'])) #period
T1=dt*(Nsize) #full period
v=(d['speed'])
X = v*T1 #full distance
dx = dt*v #smallest amount of distance travelled
total_t = (d['scan time']) #how long it ran
    
total_s = (d['samples requested']) #number of samples 
startpt = ((total_s - Nsize)/2) #starting point


endpt = startpt + Nsize #ending point
startpt = int(startpt)
endpt = int(endpt)

df = 1/T1
f = df*np.arange(Nsize/2)+df/2.0
fFull = df*np.arange((Nsize/2) + 1)+df/2.0


y = (d['sig0F'])
D = y[startpt:endpt] #signal
#D = np.flipud(D)

a = d['delay0F']/v
t = a[startpt:endpt] #time (used as x axis)

D = np.hanning(Nsize)*D #signal multiplied by a hanning function to improve FFT
S = np.fft.rfft(D) #fourier transform
S = S[0:-1]
u = np.abs(S) #gets rid of imaginary part of fourier transform solely for the plot
dNu = 1/(Nsize*dx)
Nu = dNu*np.arange(Nsize/2)


f, (ax1,ax2) = pl.subplots(2,1)
ax1.plot(t,D) #cut off

ax1.set_title('Interferogram')
#ax1.set_xlabel('Time(s) starting at WLF')



ax2.plot(300*Nu, u)
ax2.set_title('Fourier Transform of data')
#pl.xlim(0,2000)
ax2.set_xlabel('GHz?')
ax2.set_ylabel('Arb')
pl.tight_layout()
pl.show()

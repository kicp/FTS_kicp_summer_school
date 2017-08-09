#given two files, plots them in separate windows and then gives the option of comparing the two through division. Mira

import matplotlib.pyplot as pl
import pickle
import numpy as np
import sys

file1N = raw_input('First File Name: ') #gets file 1
with open( '../Data/' + str(file1N) , 'rb') as file1:
    d1=pickle.load(file1)
    
file2N = raw_input('Second File Name: ') #gets file 2
with open( '../Data/' + str(file2N) , 'rb') as file2:
    d2=pickle.load(file2)



def analyze_spectrum(d): 
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
        return t, D, Nu, u


t1, D1, Nu1, u1= analyze_spectrum(d1)
t2, D2, Nu2, u2= analyze_spectrum(d2)

    
#overplot the spectra without dividing them

pl.figure(1)
pl.plot(300*Nu1,u1, label=file1N)
pl.title(str(file1N)[:-4])
pl.plot(300*Nu2,u2, label=file2N)
pl.title(str(file2N)[:-4])
pl.legend()

oper = raw_input('Divide [y]/[n] : ')

#ensures the number of samples used is the same to be able to divide corresponding values
Len1 = len(Nu1)
Len2 = len(Nu2)

Nsize = min(Len1,Len2)
startpt1 = ((Len1 - Nsize)/2)
endpt1 = startpt1 + Nsize

startpt2 = ((Len2-Nsize)/2)
endpt2 = startpt2 + Nsize
# divide the two spectra
if str(oper) == 'y': 
    u3 = np.divide(u1[startpt1:endpt1],u2[startpt2:endpt2])
    pl.figure(3)
    pl.plot(300*Nu1[startpt1:endpt1], u3)
    pl.title('Divided spectra' )

pl.show()

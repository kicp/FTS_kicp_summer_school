import matplotlib.pyplot as pl
import pickle
import numpy as np
import sys

file1N = raw_input('First File Name: ')
with open( '../Data/' + str(file1N) , 'rb') as file1:
    d1=pickle.load(file1)
    
file2N = raw_input('Second File Name: ')
with open( '../Data/' + str(file2N) , 'rb') as file2:
    d2=pickle.load(file2)
    
X1=d1['delay0F']
Y1=d1['sig0F']

X2=d2['delay0F']
Y2=d2['sig0F']

pl.figure(1)
pl.plot(X1,Y1)
pl.title(str(file1N)[:-4])

pl.figure(2)
pl.plot(X2,Y2)
pl.title(str(file2N)[:-4])

oper = raw_input('Divide [y]/[n] : ')
Len1 = len(Y1)
Len2 = len(Y2)

Nsize = min(Len1,Len2)
startpt1 = ((Len1 - Nsize)/2)
endpt1 = startpt1 + Nsize

startpt2 = ((Len2-Nsize)/2)
endpt2 = startpt2 + Nsize

if str(oper) == 'y': 
    X3 = np.divide(X1[startpt1:endpt1],X2[startpt2:endpt2])
    pl.figure(3)
    pl.plot(X3,Y1)
    pl.title(str(file1N)[:-4] +'/'+str(file2N)[:-4] )


pl.show()

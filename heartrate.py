from pylab import *
import scipy.signal as signal
import numpy as np
from peakdetect import _smooth, peakdetect

file = open('s102.txt')
s101 = list()

for line in file:
	handle = line.rstrip().split()
	MLII, Vn = handle
	s101.append(float(MLII))
	
handle = s101[0:1801]
input = np.asarray(handle)
y = _smooth(input)

peaks = peakdetect(y,lookahead = 100, delta = 0.2)
a,b = peaks
print 'heart rate:', float(len(a))/5*60, ' bpm'

plot(y)
show()

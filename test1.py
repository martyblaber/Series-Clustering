%matplotlib inline
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(631)
np.random.seed(631)

####################################
# From: http://alexminnaar.com/time-series-classification-and-clustering-with-python.html
def DTWDistance(s1, s2):
    DTW={}

    for i in range(len(s1)):
        DTW[(i, -1)] = float('inf')
    for i in range(len(s2)):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])

    return sqrt(DTW[len(s1)-1, len(s2)-1])

#####################################

#Number of samples
nSamples=10

#Range of possible sample lengths
minTime=100
maxTime=300

#There will be a flat portion of the data.
flatMean=0.0
flatSigma=20

#Then there will be an up/down tick, with a slope.
slopeMean=2.0
slopeSigma=0.5

samples=[]

fig1=plt.figure()

for iSample in range(nSamples):
    
    #Create time series of variable length
    timeTotal=np.random.randint(minTime,high=maxTime)
    
    #Set a random starting point for an up/down-tick (in the middle half of the data)
    timeFlat=int(np.random.randint(int(timeTotal/4.),high=int(3.*timeTotal/4.)))
    
    #Set a random value before the up/down-tick
    startingValueAtT0=np.random.normal(flatMean,flatSigma)
    #Set a random slope for the up/down-tick
    slopeAfterTimeFlat=random.choice((-1, 1))*np.random.normal(slopeMean,slopeSigma)
    
    #Initiialise the whole array by setting the whole array to the starting point
    series=np.ones(timeTotal)*startingValueAtT0
    
    #for all times after timeFlat, add the up/down tick (because our time
    # unit is 1, we can just add the slope to the previous time point continuously)
    for i in range(timeFlat,timeTotal):
        series[i]=series[i-1]+slopeAfterTimeFlat
        
    #Plot the series against a list of 1,2,3,...,n2
    plt.plot(np.array(range(timeTotal)),series)
plt.show()
        
    

import numpy as np
from numpy.random import randn
def fun(Deviations,sampleSize):
    for j in range(len(Deviations)):
        for i in sampleSize:       
            Deviations[j]+=1 if (-((j+1)) < i and (j+1) > i) else False
        Deviations[j]=Deviations[j]/len(sampleSize)   
    print(Deviations)
    print(np.average(sampleSize))
fun([0,0,0],randn(100000))
 

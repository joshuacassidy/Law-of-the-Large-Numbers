import numpy as np
from numpy.random import randn

def fun(Deviations,sampleSize):
    for j in range(len(Deviations)):
        #Formatting the standard deviations being looked at (68%,95% and 99.7%) into a string by using a single line generator and checking if the number is within the range of the deviation, then expressing that deviation in percentage form with two decimal spaces.    
        Deviations[j]= "for {0} Standard deviations {1}%,".format(j+1,str(round(np.sum([Deviations[j]+1 if (-((j+1)) < i and (j+1) > i) else 0 for i in sampleSize])/len(sampleSize)*100,2)))

    print("\nThe standard deviations for the sample size of {0} randomly generated normally distributed numbers are: {1}. The average of these numbers are {2}.\n".format(len(sampleSize)," ".join(Deviations),np.average(sampleSize)))
fun([0,0,0],randn(int(input('\nWhat is the sample size of the randomly generated normally distributed numbers? \n'))))
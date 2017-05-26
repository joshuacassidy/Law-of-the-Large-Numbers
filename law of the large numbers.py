import numpy as np
from numpy.random import randn

def main(OneDeviation,TwoDeviations,ThreeDeviations,one,two,three,sampleSize):

    for i in randn(sampleSize):
            
        OneDeviation+=1 if (-(one) < i and one > i) else False
        TwoDeviations+=1 if(-(two) < i and two > i) else False
        ThreeDeviations+=1 if(-(three) < i and three > i) else False
    OneDeviation=OneDeviation/(sampleSize/100)
    TwoDeviations=TwoDeviations/(sampleSize/100)
    ThreeDeviations=ThreeDeviations/(sampleSize/100)
    print(OneDeviation,TwoDeviations,ThreeDeviations)

main(0,0,0,1,2,3,100000)
 



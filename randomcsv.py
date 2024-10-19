#!/ usr/bin/env python3

import random
import csv
import numpy as np

def randomcsv():

###100 random integars between 1 and 1000
    datatemp = []
    for i in range(0,100):
        n=random.randint(0,100)
        datatemp.append(n)
    temp_array = np.array(datatemp)
    print(temp_array)

###100 random integars between 1 and 100
    datahumid = []
    for i in range(0,100):
        n=random.randint(1,100)
        datahumid.append(n)
    humid_array = np.array(datahumid)
    print(humid_array)

###saving the arrays in a csv file in columns
    np.savetxt('random.csv', [p for p in zip(temp_array, humid_array)],delimiter=',')



##calling the function
randomcsv()   
   
   

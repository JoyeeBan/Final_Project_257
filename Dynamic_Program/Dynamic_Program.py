from ctypes import sizeof
import time
import random
from numpy.random import randint
import matplotlib.pyplot as plt
from numpy.random import seed
import numpy as np
def dynamic(arr,n):
    table=[[0 for i in range(n)]
           for i in range(n)]
    for gap in range(n):
        for j in range(gap,n):
            i=j-gap
            x=0
            if((i+2)<=j):
                x=table[i+2][j]
            y=0
            if((i+1)<(j-1)):
                y=table[i+1][j-1]
            z=0
            if(i<=(j-2)):
                z=table[i][j-2]
            table[i][j]=max(arr[i]+min(x,y),
                            arr[j] +min(y,z))
    return table[0][n-1]
if __name__ == '__main__':
    elements=list()
    times=list()
    SIZE=int(input("Enter the size of the list:\n 10,100,1000,10000,100000,1000000\n"))
for i in range(1,4):
        np.random.seed(100)
        a=np.random.randint(1,6*i,SIZE*i)
        print(a)
        start=time.process_time()
        print("The maximum money Player A (myself) is guranteed to win is:",dynamic(a,len(a)))
        end=time.process_time()
        print("Time taken for test case of length",len(a),"is:",end-start)
        elements.append(len(a))
        times.append(end-start)
plt.xlabel('List length')
plt.ylabel('Time Complexity')
plt.plot(elements,times,label='Coin Game')
plt.grid()
plt.legend()
plt.show()
plt.show()
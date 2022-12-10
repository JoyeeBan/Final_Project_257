
from ctypes import sizeof
import time
import random
from numpy.random import randint
import matplotlib.pyplot as plt
from numpy.random import seed
import numpy as np

def findMaxCoins(coin,i,j):
    if i==j:
        return coin[i]
    if i+1==j:
        return max(coin[i],coin[j])

    left=coin[i] + min(findMaxCoins(coin,i+2,j),
                        findMaxCoins(coin,i+1,j-1))

    right=coin[j] + min(findMaxCoins(coin,i+1,j-1),
                      findMaxCoins(coin,i,j-2))
    return max(left,right)

if __name__ == '__main__':
    elements=list()
    times=list()
    SIZE=int(input("Enter the size of the list:\n 10,100,1000,10000,100000\n"))
    for i in range(1,4):
        np.random.seed(100)
        a=np.random.randint(1,6*i,SIZE*i)
        print(a)
        start=time.process_time()
        print("The maximum money Player A (myself) is guranteed to win is:",findMaxCoins(a,0,len(a)-1))
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
        



   
        

    

    


    

       
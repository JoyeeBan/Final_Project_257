from ctypes import sizeof
import time
import random
from numpy.random import randint
import matplotlib.pyplot as plt
from numpy.random import seed
import numpy as np
def Greedy(coins,A,B,low,high):
    for turn in range(0,len(coins)):
        if turn % 2 == 0:
            maximum=max(coins[low],coins[high])
            A.append(maximum)
            #print("Player A chose:",maximum)

            if maximum ==coins[low]:
                low=low+1
            else:
                high=high-1

        else:
            maximum=max(coins[low],coins[high])
            B.append(maximum)
            #print("Player B chose:",maximum)
            

            if maximum==coins[low]:
                low=low+1
            else:
                high=high-1
    print("\nPlayer A's max score:",sum(A))
    print("\nPlayer B's max score:",sum(B))
if __name__ == '__main__':
    A=[]    
    B=[]
    elements=list()
    times=list()
    SIZE=int(input("Enter the size of the list:\n 10,100,1000,10000,100000,1000000\n"))
    for i in range(1,4):
        np.random.seed(100)
        a=np.random.randint(1,6*i,SIZE*i)
        print(a)
        start=time.process_time()
        print(Greedy(a,A,B,0,len(a)-1))
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

    
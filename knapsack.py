# Uses python3
import numpy as np


def optimal_weight(n , w):
    V = np.zeros(shape=(n[1] + 1, n[0] + 1), dtype=int)
    for i in range(1 , n[1] + 1):
        for j in range(1 ,n[0] + 1):
           if(w[i-1] <= j):
               V[i,j] = max(V[i-1,j] , V[i-1 , j - w[i-1]] + w[i-1])
           else:
               V[i,j] = V[i-1 , j]
    return V[n[1] , n[0]]

    

if __name__ == '__main__':
    n = list(map(int , input().split()))
    w = list(map(int , input().split()))
    print(optimal_weight(n,w))
    

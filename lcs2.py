#Uses python3

import numpy as np

def lcs2(n1,n2,num1,num2):
    D = np.zeros(shape=(n1 + 1, n2 + 1), dtype=int)

    for i in range(1,n1 + 1):
        for j in range(1,n2+ 1):
            if num1[i-1] == num2[j-1]:
                D[i,j] = D[i-1,j-1] + 1
            else:
                D[i,j] = max(D[i-1, j] , D[i,j-1])
    return D[n1,n2]
    

if __name__ == '__main__':
    n1 = int(input())
    num1 = list(map(int , input().split()))
    n2 = int(input())
    num2 = list(map(int , input().split()))
    print(lcs2(n1,n2,num1,num2))
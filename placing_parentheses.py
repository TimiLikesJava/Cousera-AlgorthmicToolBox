# Uses python3
import numpy as np
from math import inf
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinandMax(D ,V , i , j , opts):
    min_V = inf
    max_V = -inf
    for k in range(i,j):
        a = evalt(V[i,k] , V[k+1,j] , opts[k])
        b = evalt(V[i,k] , D[k+1 , j] , opts[k])
        c = evalt(D[i,k] , V[k+1 , j] , opts[k])
        d = evalt(D[i,k] , D[k+1 , j] , opts[k])
        min_V = min(min_V , a ,b,c,d)
        max_V = max(max_V , a ,b, c,d)
    return min_V,max_V

def get_maximum_value(opds , opts):
    D = np.zeros(shape=(len(opds) , len(opds)), dtype=int) # min
    V = np.zeros(shape=(len(opds) , len(opds)), dtype=int) # max

    num = len(opds)

    for i in range(num):
        D[i,i] = opds[i]
        V[i,i] = opds[i]

    for s in range(1 , num):
        for i in range(0 , num - s):
            j = i + s
            D[i,j] , V[i,j] = MinandMax(D , V , i,j,opts)

    return V[0,num-1]


if __name__ == "__main__":
    data = input()
    opds = []
    opts = []

    for i in data:
        if i in ['+' , '-' , '*']:
            opts.append(i)
        else:
            opds.append(i)

    print(get_maximum_value(opds , opts))

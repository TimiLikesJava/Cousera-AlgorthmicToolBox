import operator
import math

def get_optimal_value(capacity, weights, values):
    value = 0
    for _ in range(n):
        if(capacity == 0):
            return value
        num = digit(weights,values)
        if (num >= 0):

            a = min(weights[num] , capacity)
            value = value + (a*(values[num]/weights[num]))
            capacity = capacity - a
            weights[num] = weights[num] - a
    return value


def digit(weights,values):
    index = -1
    maxN = 0
    for i in range(n):
        if(weights[i] > 0 and (values[i]/weights[i]) > maxN):
            maxN = values[i]/weights[i]
            index = i
    return index



if __name__ == "__main__":
    data = list(map(int,input().split()))
    n, capacity = data[0:2]
    values = [0]*n
    weights = [0]*n
    for i in range(n):
        values[i], weights[i] = map(int, input().split())
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


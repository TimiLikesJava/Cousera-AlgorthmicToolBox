# Uses python3
def calc_fib(n):
    array = [0,1]

    for i in range(2 , n+1):
        array.append(array[i-1] + array[i-2])

    result = array[n]
    return result

n = int(input())
print(calc_fib(n))

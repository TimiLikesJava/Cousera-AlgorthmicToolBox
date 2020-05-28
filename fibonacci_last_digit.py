# Uses python3
def lastDigit(n):
    array = [0,1]

    for i in range(2, n+1):
        thing = array[i-1] + array[i-2]
        array.append(thing % 10)

    result = array[n]
    return result




if __name__ == "__main__":
    n = int(input())
    print(lastDigit(n))

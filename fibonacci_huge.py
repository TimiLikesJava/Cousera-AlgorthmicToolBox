def pisano(m):
    prev , curr = 0 , 1

    for i in range(0 , m*m):
        prev , curr = curr , (prev+curr) % m

        if(prev == 0 and curr == 1):
            return i + 1


    

def fib(n, m):
    array = [0,1]

    n = n % pisano(m)

    for i in range(2 , n+1):
        array.append(array[i-1] + array[i-2])

    current = array[n] % m
    

    return current


if __name__ == "__main__":
    n, m = map(int , input().split())
    print(fib(n,m))
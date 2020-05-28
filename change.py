def moneyChange(n):
    count = 0

    while( n > 0):
        if(n >= 10):
            count = count + (n // 10)
            n = n % 10
        if(n >= 5 and n < 10):
            count = count + (n//5)
            n = n % 5
        if(n >= 1 and n < 5):
            count = count + (n // 1)
            n = n % 1


    return count



if __name__ == "__main__":
    n = int(input())
    print(moneyChange(n))
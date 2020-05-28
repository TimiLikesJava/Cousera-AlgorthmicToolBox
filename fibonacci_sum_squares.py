import math


def fibSquare(n):
    
    if(n == 0):
        sum = 0
    elif(n == 1):
        sum = 1
    else:

        sum = 1



        for i in range(2,n+1):
            sqrt5 = math.sqrt(5)
            F_n = int((( (1 + sqrt5) ** i - (1 - sqrt5) ** i ) / ( 2 ** i * sqrt5 )))
            F_n = F_n ** 2
            sum = sum + F_n


   

    
    return sum % 10



if __name__ == "__main__":
    n = int(input())
    print(fibSquare(n))
    
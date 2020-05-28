import math
def fibSum(n):
    
    sqrt5 = math.sqrt(5)

    if(n == 0):
        sum = 0
    elif(n == 1):
        sum = 1
    else:
        sum = 1
        for i in range(2 , n+1):
            F_n = int((( (1 + sqrt5) ** i - (1 - sqrt5) ** i ) / ( 2 ** i * sqrt5 )))
            sum = sum + F_n
        


    

    return sum % 10


   



if __name__ == "__main__":
    m = int(input())
    print(fibSum(m))

    

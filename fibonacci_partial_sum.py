def fibSum(a,b):
    array = [0,1]
    if(a == 0):
        sum = 0
    elif(a == 1 ):
        sum = 1
    else:
        sum = 1
        for i in range(2,b+1):
            array.append(array[i-1] + array[i-2])
            

    for j in range(a,b+1):
        sum = sum + array[j]
    


    

    current = sum % 10
    return current


if __name__ == "__main__":
    m,n = map(int , input().split())
    print(fibSum(m,n))

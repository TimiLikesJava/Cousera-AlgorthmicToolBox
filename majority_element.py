 
def majorityElement(arr , lo , hi):
    if(lo == hi):
        return arr[lo]

    mid = (lo + hi) // 2

    left = majorityElement(arr, lo , mid)
    right = majorityElement(arr, mid+1 , hi)

    if(left == right):
        return left
    
    lCount = count(left , arr , lo , hi)
    rCount = count(right , arr , lo , hi)

    if(lCount > rCount):
        return lCount

    else:
        return rCount

def count(num , arr , lo , hi):
    count = 0
    for i in range(len(arr)):
        if(arr[i] == num):
            count += 1
        if(count > len(arr)//2):
            return num
        else:
            return -1


def majorStuff(arr , n):
    my_dict = {}

    for num in arr:
        if num not in my_dict:
            my_dict[num] = 1
        if my_dict[num] > len(arr) // 2:
            return 1
        else:
            my_dict[num] += 1

    return 0
        



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    print(majorStuff(a,n))
  

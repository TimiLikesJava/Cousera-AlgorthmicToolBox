from math import inf
def DPChange(money):
    coins = [1,3,4]

    MinNumCoins = [None] * (money + 1)
    MinNumCoins[0] = 0

    for i in range(1 , money+1):
        MinNumCoins[i] = inf
        for j in coins:
            if i >= j:
                numCoins = MinNumCoins[i - j] + 1
                if numCoins < MinNumCoins[i]:
                    MinNumCoins[i] = numCoins
    
    return MinNumCoins[i]






if __name__ == '__main__':
    money = int(input())
    print(DPChange(money))

def gcd(a,b):
    if b == 0:
        return a

    return gcd(b , a%b)


def lcm(a,b):
    lcm = int(a*b / gcd(a,b))
    return lcm



if __name__ == "__main__":
    x , y = map(int , input().split())
    print(lcm(x,y))



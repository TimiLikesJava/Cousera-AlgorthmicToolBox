# python3



def compute_min_refills(distance, tank, stops):
    nR = 0
    nC = 0
    while(nC <= len(stops)):
        lR = nC
        while(nC <= len(stops) and  stops[nC+1] - stops[lR] <= tank):
             nC = nC + 1
        if(nC == lR):
            return -1
        if (nC < len(stops)):
            nR = nR + 1    
    return nR

if __name__ == '__main__':
    d = 950
    m = 400
    stops = [0 , 200 , 375 , 550 , 750 , 950]
    print(compute_min_refills(d, m, stops))




def max_pairwise_product(numbers):
    max_p = 0
    second_max = 0
    index1 = 0
    index2 = 0

    if(len(numbers) == 1):
        return "Bad Constraint"

    for i in range(len(numbers)):
        if(numbers[i] > max_p):
            max_p = numbers[i]
            index1 = i

    for j in range(len(numbers)):
        index2 = j
        if(index2 == index1):
            index2 += 1
        
        if(index2 < len(numbers)):
            if(numbers[index2] > second_max and second_max < max_p):
                second_max = numbers[index2]
        


        

    return max_p * second_max



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

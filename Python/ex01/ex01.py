# all tests will have at least 1 element in the list

def mean(numbers: list):
    return sum(numbers) / len(numbers)

def median(numbers: list): 
    if(len(numbers) % 2 == 0):
        return (numbers[int(len(numbers)/ 2)] + numbers[int(len(numbers)/ 2 - 1)]) / 2
    else:
        return numbers[int(len(numbers)/ 2)]

# should return the smallest mode if there are ties (0, 0, 1, 2, 3, 4, 4) should return 0
def mode(numbers: list): 
    mostCommonNum = numbers[0]
    maxCount = numbers.count(mostCommonNum)
    for num in numbers:
        count = numbers.count(num)
        if(count > maxCount):
            mostCommonNum = num
            maxCount = count

    return mostCommonNum


# 0 1 2 3 4 5
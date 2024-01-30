def add(num1, num2):
    return num1 + num2


# return mean of numbers
# reutnr 0 if numbers is empty
def mean(numbers):
    if(len(numbers) == 0): return 0
    return sum(numbers) / len(numbers)

def mode(numbers):
    numOccurrences = dict()
    for num in numbers:
        if(num in numOccurrences):
            numOccurrences[num] += 1
        else:
            numOccurrences[num] = 1
    return max(numOccurrences, key=numOccurrences.get)

def median(numbers):
    numbers.sort()
    if(len(numbers) % 2 == 0):
        return (numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2)]) / 2
    else:
        return numbers[int(len(numbers) / 2)]
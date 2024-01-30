def add(num1, num2):
    return num1 + num2


# return mean of numbers
# reutnr 0 if numbers is empty
def mean(numbers):
    return sum(numbers) / len(numbers)

def mode(numbers):
    numOccurrences = dict()
    for num in numbers:
        numOccurrences[num] += 1

def median(numbers):
    numbers.sort()
    if(len(numbers) % 2 == 0):
        return (numbers[len(numbers) / 2] + numbers[len(numbers) / 2]) / 2
    else:
        return numbers[len(numbers) / 2]
import math
import statistics

def add(num1, num2):
    return num1 + num2


# return mean of numbers
# reutnr 0 if numbers is empty
def average(numbers):
    if(len(numbers) == 0): return 0
    return sum(numbers) / len(numbers)

def modeFunction(numbers):
    return statistics.mode(numbers)

def medianFunction(numbers):
    numbers.sort()
    if(len(numbers) % 2 == 0):
        return (numbers[int(len(numbers) / 2) - 1] + numbers[int(len(numbers) / 2)]) / 2
    else:
        return numbers[int(len(numbers) / 2)]

def percentile(numbers):
    return
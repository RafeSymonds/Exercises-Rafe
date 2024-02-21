import math
import statistics

def fibonacciCalculator(index: int):
    # counter = 3
    # values = [0, 1, 1]
    # while(counter < index + 1):
    #     values.append(values[counter-1] + values[counter-2])
    #     counter += 1
    # return values[index]
    

    if(index == 0):
        return 0
    if(index == 1 or index == 2):
        return 1
    return fibonacciCalculator(index -1) + fibonacciCalculator(index - 2)


# add your own tests below and run with "python3 Python/ex01/ex01.py"
# no output means your tests passed
# tests can look like this or you can print them
# assert(fibonacciCalculator(1) == 1)

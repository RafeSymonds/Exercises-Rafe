import sys
sys.path.append("Python/ex05")

import ex05

def test_fibonacciCalculator():
    assert ex05.fibonacciCalculator(0) == 0
    assert ex05.fibonacciCalculator(1) == 1
    assert ex05.fibonacciCalculator(2) == 1
    assert ex05.fibonacciCalculator(3) == 2
    assert ex05.fibonacciCalculator(4) == 3
    assert ex05.fibonacciCalculator(5) == 5
    assert ex05.fibonacciCalculator(6) == 8
    assert ex05.fibonacciCalculator(7) == 13
    assert ex05.fibonacciCalculator(8) == 21
    assert ex05.fibonacciCalculator(29) == 514229
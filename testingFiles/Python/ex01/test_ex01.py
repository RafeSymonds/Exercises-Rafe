import sys
sys.path.append("Python/ex01")

import ex01

def test_fibonacciCalculator():
    assert ex01.fibonacciCalculator(0) == 0
    assert ex01.fibonacciCalculator(1) == 1
    assert ex01.fibonacciCalculator(2) == 1
    assert ex01.fibonacciCalculator(3) == 2
    assert ex01.fibonacciCalculator(4) == 3
    assert ex01.fibonacciCalculator(5) == 5
    assert ex01.fibonacciCalculator(6) == 8
    assert ex01.fibonacciCalculator(7) == 13
    assert ex01.fibonacciCalculator(8) == 21

def test_test_fibonacciCalculator_heavy():
    assert ex01.fibonacciCalculator(50) == 12586269025
    #assert ex01.fibonacciCalculator(100) == 354224848179261915075
    #assert ex01.fibonacciCalculator(500) == 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
    pass
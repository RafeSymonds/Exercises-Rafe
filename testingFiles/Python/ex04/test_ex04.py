from Python.ex04 import ex04

def test_fibonacciCalculator():
    assert ex04.mergeArrays([1],[1]) == [1,1]
    assert ex04.mergeArrays([3,4,8,9,2345],[1,12,345,3456345]) == [1,3,4,8,9,12,345,2345,3456345]
    assert ex04.mergeArrays([2], [1]) == [1,2]
from Python.ex01 import ex01

def test_mean():
    assert ex01.mean([1,2]) == 1.5
    assert ex01.mean([1,2,3]) == 2
    assert ex01.mean([1]) == 1

def test_median():
    assert ex01.median([1,2]) == 1.5
    assert ex01.median([1,2,3]) == 2
    assert ex01.median([1,2,3,4]) == 2.5
    assert ex01.median([1]) == 1
    assert ex01.median([1,2,3,4,5]) == 3
    assert ex01.median([1,2,3,4,5,6]) == 3.5

def test_mode():
    assert ex01.mode([1,2]) == 1
    assert ex01.mode([1]) == 1
    assert ex01.mode([1,1,1,2,2,2]) == 1
    assert ex01.mode([1,2,3,4,5,6,7,7,7]) ==7
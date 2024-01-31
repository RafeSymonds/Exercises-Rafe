import ex01

def test_add():
    assert ex01.add(5,10) == 15
    assert ex01.add(2,5) == 7
    assert ex01.add(8,10) == 18
    assert ex01.add(-6,1) == -5

def test_mean():
    assert ex01.mean([5,4,3,2,1]) == 3
    assert ex01.mean([1]) == 1
    assert ex01.mean([]) == 0
    
def test_mode():
    assert ex01.mode([5,4,3,2,1, 6, 1]) == 1
    assert ex01.mode([1]) == 1

        
def test_median():
    assert ex01.median([5,4,3,2,1]) == 3
    assert ex01.median([1]) == 1
    assert ex01.median([1,2]) == 1.5
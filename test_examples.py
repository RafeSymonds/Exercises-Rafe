import pythontest

def test_add():
    assert pythontest.add(5,10) == 15
    assert pythontest.add(2,5) == 7
    assert pythontest.add(8,10) == 18
    assert pythontest.add(-6,1) == -5

def test_mean():
    assert pythontest.mean([5,4,3,2,1]) == 3
    assert pythontest.mean([1]) == 1
    assert pythontest.mean([]) == 0
    
def test_mode():
    assert pythontest.mode([5,4,3,2,1, 6, 1]) == 1
    assert pythontest.mode([1]) == 1

        
def test_median():
    assert pythontest.median([5,4,3,2,1]) == 3
    assert pythontest.median([1]) == 1
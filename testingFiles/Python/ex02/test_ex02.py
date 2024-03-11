from Python.ex02 import ex02

def test_1():
    student1 = ex02.Student("Alice")
    student1.add_grade("Math", 90)
    student1.add_grade("Science", 85)
    student1.add_grade("History", 95)

    highest, lowest = student1.calculate_highest_lowest_grades()
    assert highest == ("History", 95)
    assert lowest == ("Science", 85)
    grades = student1.display_grades()
    
    assert grades == 'Math: 90\nScience: 85\nHistory: 95\n'

    average = student1.calculate_average_grade()
    assert average == 90

def test_2():
    student1 = ex02.Student("Bob")

    highest, lowest = student1.calculate_highest_lowest_grades()
    assert highest == None
    assert lowest == None
    grades = student1.display_grades()
    assert grades == ''
    average = student1.calculate_average_grade()
    assert average == None

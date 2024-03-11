class Student:
    # grades is a list of tuples in the form of (subject, grade)
    def __init__(self, name: str):
        self.name = name
        self.grades = []
    
    # add a tuple of (subject, grade) to grades
    def add_grade(self, subject: str, grade: int):
        self.grades.append((subject, grade))

    # return None if there are no grades
    # otherwise return the average grade
    def calculate_average_grade(self):
        if(len(self.grades) == 0):
            return None
        return sum(subjectGrade[1] for subjectGrade in self.grades) / len(self.grades)

    # return a string that is in the format '<subject>: <grade>'
    # each subject should be on a different line
    # return an empty string if there are no grades
    def display_grades(self):
        output = ''
        for subject, grade in self.grades:
            output += f"{subject}: {grade}\n"
        return output

    # return a tuple of (None, None) if there are no grades
    # otherwise return a tuple of (HighestGrade, LowestGrade)
    def calculate_highest_lowest_grades(self):
        if(len(self.grades) == 0):
            return None, None
        highest = max(self.grades, key=lambda x: x[1])
        lowest = min(self.grades, key=lambda x: x[1])
        return highest, lowest 
    


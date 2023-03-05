'''
Write a Student class with instance variables:

student_id: int
first_name: str
last_name: str
exam_scores: list[int]

The constructor takes student_id, first_name, and last_name in order to initialize the class.
The exam_scores must be initialized as an empty list.
methods:
    add_score(score): adds score to the list exam_scores. The score is any number in [0, 100]
    show_scores(): displays all student scores in one row
    score_average(): returns student's average score, or prints a message that the student didn't pass any exam yet
    course_passed(): if student collects three scores > 60 points, the method returns True, else method returns False
'''


class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, exam_scores=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = []

    def __str__(self):
        return f"{self.student_id}, {self.first_name}, {self.last_name}"

    def __repr__(self):
        return f"""Student id - {self.student_id}
Student name - {self.first_name}
Student surname - {self.last_name}"""

    def add_score(self, score):
        if score < 0 or score > 100:
            redact_wrong_score = int(input("Введите соответсвующее число "))
            if redact_wrong_score < 0 or redact_wrong_score > 100:
                return "Вновь введено неверное число"
            self.exam_scores.append(redact_wrong_score)
            return "Оценка исправлена и добавлена"
        else:
            self.exam_scores.append(score)
            return "Оценка успешно добавлена"

    def show_scores(self):
        row_scores = ', '.join(map(str, self.exam_scores))
        return row_scores

    def score_average(self):
        if len(self.exam_scores) != 0:
            length = len(self.exam_scores)
            summa = sum(self.exam_scores)
            return round(summa / length, 2)
        else:
            return "The student didn't pass any exam yet"

    def course_passed(self):
        if len(self.exam_scores) == 3:
            for i in self.exam_scores:
                if i > 60:
                    return True
                else:
                    return False
        else:
            return None


st1 = Student(1, "Ivanov", "Ivan")
print(st1.__repr__())
print(st1.add_score(12))
print(st1.add_score(56))
print(st1.add_score(73))
print(st1.score_average())
print(st1.show_scores())
print(st1.course_passed())
print("!" * 100)
st2 = Student(2, "Igorev", "Igor")
print(st2.add_score(59))
print(st2.add_score(23))
print(st2.add_score(45))
print(st2.score_average())
print(st2.show_scores())
print(st2.course_passed())
print("!" * 100)
st3 = Student(3, "Elon", "Musk")
print(st3.add_score(90))
print(st3.add_score(69))
print(st3.add_score(70))
print(st3.score_average())
print(st3.show_scores())
print(st3.course_passed())

# Todo
"""__method__ str i repr
obernut' v try, except
score_average.divbyzero podumat' 
potom vigruzit na github s nazvaniem student_class_excercise"""

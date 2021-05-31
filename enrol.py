

from course import Course

from student import Student

from datetime import datetime


class Enrol:

    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise TypeError("Invalid Student...")

        if not isinstance(course, Course):
            raise TypeError("Invalid Course")

        self._student = student
        self._course = course
        self._grade = None
        self._date = datetime.now()

    def set_grade(self, grade):
        self._grade = grade

    def get_grade(self):
        return self._grade


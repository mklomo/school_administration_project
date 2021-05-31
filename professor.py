"""
    This script implements the professor class
"""

from person import Person

from course import Course


class Professor(Person):
    """
UUID : int

_salary_per_annum : float

_courses_thought

add_bonus() : float
    """
    _PROFESSOR_ID = 8000

    def __init__(self, salary_per_annum, first_name, last_name, date_of_birth, phone_number, address):
        super().__init__(first_name, last_name, date_of_birth, phone_number, address)
        self._UUID = Professor._PROFESSOR_ID
        self._salary_per_annum = salary_per_annum
        self._courses_taught = []
        self._got_raise = False
        Professor._PROFESSOR_ID += 1

    def check_bonus(self):
        if len(self._courses_taught) >= 4 and self._got_raise is False:
            self._salary_per_annum += 15000
            self._got_raise = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("Invalid Course...")

        else:
            self._courses_taught.append(course)

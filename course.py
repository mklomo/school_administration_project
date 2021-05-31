"""
    This script implements the course Class
"""
from professor import Professor

from enrol import Enrol


class Course:
    """
_min_number_of_students : int

_max_number_of_students : int

_course_code : int

_start : date

_end : date

_name : str

_semester : int

is_cancelled() : boolean

get_num_students_enrolled() : int
  """

    def __init__(self, min_number_of_students, max_number_of_students, course_code, start_date,
                 end_date, name, professor):
        self._min_number_of_students = min_number_of_students
        self._max_number_of_students = max_number_of_students
        self._course_code = course_code
        self._start_date = start_date
        self._end_date = end_date
        self._name = name
        self._enrollments = []
        self._professors = []
        if isinstance(professor, Professor):
            self._professors.append(professor)

        elif isinstance(professor, list):
            for entry_professor in professor:
                if not isinstance(entry_professor, Professor):
                    raise TypeError("Invalid Professor...")

            self._professors.append(entry_professor)

        else:
            raise TypeError("Invalid Professor..")

    def is_cancelled(self):
        return len(self._enrollments) < self._min_number_of_students

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise TypeError("Invalid Professor Entry...")

        else:
            self._professors.append(professor)

    def enroll_course(self, enrol):
        if not isinstance(enrol, Enrol):
            raise TypeError("Invalid Enroll")

        if len(self._enrollments) == self._max_number_of_students:
            raise RuntimeError("Can not enroll in course, course is full..")

        self._enrollments.append(enrol)

    def get_enrollment_numbers(self):
        return len(self._enrollments)

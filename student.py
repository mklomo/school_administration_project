from person import Person

from enrol import Enrol


class Student(Person):
    """
_is_international : boolean

_is_full_time() : boolean

is_on_probation() : boolean

   """

    _STUDENT_ID = 1000000

    def __init__(self, first_name, last_name, date_of_birth, phone_number, address, international=False):
        super().__init__(first_name, last_name, date_of_birth, phone_number, address)
        self._uuid = Student._STUDENT_ID
        self._international = international
        self._enrolled = []
        self._is_on_probation = False
        Student._STUDENT_ID += 1

    def add_enrollment(self, enrol):
        if not isinstance(enrol, Enrol):
            raise TypeError("Invalid Enrol...")

        else:
            self._enrolled.append(enrol)

    def is_on_probation(self):
        student_grade_list = []
        for enrol_entry in self._enrolled:
            # Get the student Grades
            course_grade = enrol_entry.get_grade()
            student_grade_list.append(course_grade)

        sum_of_grades = sum(student_grade_list)

        total_of_grades = len(student_grade_list) * 100

        average = sum_of_grades/total_of_grades

        if average < 0.4:
            self._is_on_probation = True

    def is_full_time(self):
        if len(self._enrolled) <= 2:
            return False
        else:
            return True

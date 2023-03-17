class Student:
    school_name = None
    school_address = None


    def __init__(self, stu_id, student_name=None, student_mailid=None, student_percentage=None):
        self.student_id = stu_id
        self.student_name = student_name
        self.student_mailid = student_mailid
        self.student_percentage = student_percentage

    @property
    def get_student_name(self):
        return self.student_name

    # create a non-static method to return Hi, jack - Your percentage is 45.2
    @property
    def get_name_with_percentage(self):
        return "Hi, " + self.student_name + " - Your percentage is " + str(self.student_percentage)

    @staticmethod
    def get_school_detail():
        return Student.school_name + " is located at " + Student.school_address

    def print_grade(self):
        if self.student_percentage > 100 or self.student_percentage < 0:
            print("Invalid input")
        elif self.student_percentage >= 90:
            print("Grade A")
        elif self.student_percentage >= 80 and self.student_percentage <= 89:
            print("Grade B")
        elif self.student_percentage >= 60 and self.student_percentage <= 79:
            print("Grade C")
        else:
            print("Failed, Please re-attempt")

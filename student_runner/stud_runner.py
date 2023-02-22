from student_package.student_module import Student

Student.school_name = "Global"
Student.school_address = "Pune"

stu1 = Student(1001, "jack", "jack@gmail.com", 45.2)
stu2 = Student(student_id=1002, student_name="Peter", student_mailid="peter@gmail.com", student_percentage=98.2)
stu3 = Student(1003, "mark", "mark@gmail.com", 56.5)
stu4 = Student(1004)
stu5 = Student(1005, student_name="bala", student_percentage=98.3)

# name = stu2.get_student_name()
# print(name)

# res=stu2.get_name_with_percentage()
# print(res)
#
# print(stu2.get_name_with_percentage())
#
# print(stu5.get_name_with_percentage())

print(Student.get_school_detail())

res = stu2.get_name_with_percentage
print(res)

print(stu2.get_name_with_percentage)

print(stu2.get_student_name)

stu2.set_school_detail1=98

print(stu2.student_id)


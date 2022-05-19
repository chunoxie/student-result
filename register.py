from student import Student

name = input("\nEnter name for new Student: ")
age = input("Enter age for new student: ")
gender = input("Enter student gender: ")

test_student = Student(name, age, gender)
print(f"\nHello! My name is {test_student.name} and I'm {test_student.age} years old.")

test_student.enter_score()

print(f'\nSubjects for {test_student.name} are:\n{test_student.subjects}')
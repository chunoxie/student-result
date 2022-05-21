from student import Student

name = input("\nEnter name for new Student: ")
age = input("Enter age for new student: ")
gender = input("Enter student gender: ")

test_student = Student(name, age, gender)
print(f"\nHello! My name is {test_student.name} and I'm {test_student.age} years old.")

test_student.enter_score()

print(f'\nSubjects for {test_student.name} are:\n{test_student.subjects}')
scores_dict = test_student.subjects

header = f"""
===================================
Welcome to TechApprentice Academy.
FINAL RESULT SHEET.
-----------------------------------
Student Name:   {test_student.name}
Student Age:    {test_student.age}
Student Gender: {test_student.gender}
====================================
"""
print(header)
print('Subjects:')
average_score = 0

for x in scores_dict.keys():
    y = scores_dict[x]
    print(f'{x}: {y[-1]}')
    average_score += y[-1]

new_average = average_score / len(scores_dict)

remarks = ''
if new_average <= 40:
    remarks = 'Poor'
elif new_average > 40 and new_average <= 60:
    remarks = 'Average'
else:
    remarks = 'Good'

footer = f"""
====================================
Average: {new_average}
Comment: {remarks}
===================================
"""
print(footer)

"""
Sample output when printed:
===================================
Welcome to TechApprentice Academy.
FINAL RESULT SHEET.
-----------------------------------
Student Name: Franklyn
Student Age: 20
Student Gender: Male
====================================
Subjects:
English: 90
Maths: 99
Data Structures: 89
====================================
Average: 94.3
Comment: Excellent
===================================
"""
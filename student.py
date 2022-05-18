"""
This creates a student object.
"""
# Today, we'll explore interesting aspects of objects further. 
# We'll also see how to collaborate on GitHub
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = {}

    def speak(self):
        """
        Commands the student object to say its name and age.
        """
        print(f"Hello! My name is {self.name} and I'm {self.age} years old.")

    def enter_score(self):
        new_subjects = {}
        number_of_subjects = int(input(f"\nHow many subjects do you want to register for {self.name}? "))
        
        for i in range(number_of_subjects):
            subject_name = input(f"\nEnter name of subject - {i+1}: ")
            subject_score = int(input(f"Enter score for {subject_name}: "))
            new_subjects[subject_name] = subject_score
        self.subjects = new_subjects

    def print_scores(self):
        print(f'\nSubjects for {self.name} are:\n{self.subjects}')

test_student = Student("Testing", 25, 'Male')
test_student.speak()

test_student.print_scores()

test_student.enter_score()
test_student.print_scores()

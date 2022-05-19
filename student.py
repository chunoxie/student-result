"""
This creates a student object.
"""
# Today, we'll explore interesting aspects of objects further. 
# We'll also see how to collaborate on GitHub
# Today will be about making modules.
class Student:
    def __init__(self):
        name = input("\nEnter name for new Student: ")
        age = input("Enter age for new student: ")
        gender = input("Enter student gender: ")
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = {}

    def speak(self):
        """
        Commands the student object to say its name and age.
        """
        print(f"\nHello! My name is {self.name} and I'm {self.age} years old.")

    def enter_score(self):
        #new_subjects = {}
        number_of_subjects = int(input(f"\nHow many subjects do you want to register for {self.name}? "))
        
        for i in range(number_of_subjects):
            subject_name = input(f"\nEnter name of subject - {i+1}: ")
            subject_score = int(input(f"Enter score for {subject_name}: "))
            self.subjects[subject_name] = subject_score # what does this do please?
        #self.subjects = new_subjects

    def print_scores(self):
        print(f'\nSubjects for {self.name} are:\n{self.subjects}')

"""
This creates a student object.
"""

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        """
        Commands the student object to say its name and age.
        """
        print(f"Hello! My name is {self.name} and I'm {self.age} years old.")

clement = Student("Clement", 25, 'Male')
clement.speak()

bennie = Student("Bennie", 21, 'Female')
bennie.speak()
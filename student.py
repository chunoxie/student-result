"""
This creates a student object.
"""
# Today, we'll explore interesting aspects of objects  further. 
# We'll also see how to collaborate on GitHub
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.english_score = None
        self.maths_score = None
        self.science_score = None

    def speak(self):
        """
        Commands the student object to say its name and age.
        """
        print(f"Hello! My name is {self.name} and I'm {self.age} years old.")

    def enter_score(self, english, maths, science):
        self.english_score = english
        self.maths_score = maths
        self.science_score = science

    def print_scores(self):
        if self.english_score:
            print(f'{self.name}, your scores are as follows:\n English: {self.english_score}\n Maths: {self.maths_score}\n Science: {self.science_score}\n ')
        else:
            print(f'Seems there is no score for {self.name}.\nYou need to enter scores first.\nUse the method enter_score()')

        
bennie = Student("Bennie", 21, 'Female')
clement = Student("Clement", 25, 'Male')
samson = Student("Samson", 20, "Male")

clement.speak()
bennie.speak()
samson.speak()

samson.print_scores()
samson.enter_score(50, 70, 80)
samson.print_scores()
clement.print_scores()




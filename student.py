"""
This creates a student object.
"""
# Today, we'll explore interesting aspects of objects further. 
# We'll also see how to collaborate on GitHub
# Today will be about making modules.
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = {} 
        # {"English": [15, 15, 15, 25, 30, 100], "Maths": [15, 15, 15, 25, 30, 100]}
        
    def enter_score(self):
        """
        Here you enter the scores for the students.
        First, you'll be required to enter the number of subjects.
        Then, for each subject, you'll enter the name and 5 scores:
         - 1st test
         - 2nd test
         - 3rd test
         - midterm test
         - exam
         - The scores are computed into total and added on for each subject.
        """
        number_of_subjects = int(input(f"\nHow many subjects do you want to register for {self.name}? "))
        
        for i in range(number_of_subjects):
            subject_name = input(f"\nEnter name of subject - {i+1}: ")
            number_of_scores = 5
            score_list = []

            for x in range(number_of_scores):
                score = int(input(f"Enter score {x+1} for {subject_name}: "))
                score_list.append(score)

            total = sum(score_list)
            score_list.append(total)

            self.subjects[subject_name] = score_list
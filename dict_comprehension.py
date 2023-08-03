'''
The dictionary comprehension allows us to create a new dictionary from the values in a list or in a
dictionary
'''
import random

names = ['Angela', 'Dave', 'Martin', 'Andrea', 'Rose']

students_scores = {student:random.randint(1,100) for student in names}

print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 70}

print(passed_students)
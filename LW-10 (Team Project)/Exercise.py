# Author: Natan Nedaikhlib

try:
    # Open 'questions.txt' in write mode
    with open('questions.txt', 'w') as file:
        # Write the student's surname
        file.write('Surname: Ivanenko\n')
        # Write the programming question for the second student
        file.write('Question: Can you explain how list comprehensions work in Python?\n')
except IOError:
    # Print an error message if file operations fail
    print("Error: Unable to work with the file.")
# Second student(Sukov Mykola) reads the question and writes the answer
try:
    with open('questions.txt', 'a') as file: 
        # Write the student's surname
        file.write('Surname: Zarytska\n')
        # Provide the answer
        file.write('Answer: List comprehensions provide a concise way to create lists. \n')
        file.write('They consist of brackets containing an expression followed by a for clause, \n')
        file.write('and then zero or more for or if clauses. The result will be a new list \n')
        file.write('resulting from evaluating the expression in the context of the for and \n')
        file.write('if clauses. For example, [x**2 for x in range(10)] generates a list of \n')
        file.write('squares from 0 to 9.\n')
        # Pose a new question for the third student
        file.write('Question: What is the difference between deep copy and shallow copy in Python?\n')
except IOError:
    print("Error: Unable to work with the file.")

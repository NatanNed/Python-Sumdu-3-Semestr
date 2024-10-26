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
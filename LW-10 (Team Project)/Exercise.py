# Author: Natan Nedaikhlib

try:
    # Open 'questions.txt' in write mode
    with open('questions.txt', 'w') as file:
        # Write the student's surname
        file.write('Surname: Nedaikhlib\n')
        # Write the programming question for the second student
        file.write('Question: Can you explain how list comprehensions work in Python?\n')
except IOError:
    # Print an error message if file operations fail
    print("Error: Unable to work with the file.")

# Second student(Sukov Mykola) reads the question and writes the answer
try:
    with open('questions.txt', 'a') as file: 
        # Write the student's surname
        file.write('Surname: Sukov\n')
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

# Third student (Shapoval Anastasia) writes the answer and adds a question 
try:
    with open('questions.txt', 'a') as file:
        # Write the student's surname
        file.write('Surname: Shapoval\n')
        # Provide the answer
        file.write('Answer: In Python, a shallow copy creates a new object but only copies references to the internal objects, \n')
        file.write('so changes to those objects affect the original. In contrast, a deep copy recursively creates new \n')
        file.write('copies of all objects contained in the collection, meaning that changes to the copy do not affect the original. \n')
        file.write('Thus, deep copying ensures complete independence of the copy from the original, while shallow copying does not.\n')
        # Pose a new question for the next student
        file.write('Question: How does exception handling work in Python?\n')
except IOError:
    print("Error: Unable to work with the file.")

# Fourth student (Belikov Vladyslav Volodymyrovych) writes the answer and adds a question
try:
    with open('questions.txt', 'a') as file:
        # Write the student's surname
        file.write('Surname: Belikov\n')
        # Provide the answer
        file.write('Answer: Exception handling in Python is done using try, except, else, and finally blocks. \n')
        file.write('When an exception occurs in the try block, the code jumps to the except block. If no exception occurs, \n')
        file.write('the else block is executed. The finally block is executed no matter what, whether an exception occurred or not.\n')
        # Pose a new question for the next student
        file.write('Question: What is your favorite Python module or library, and why do you like it?\n')
except IOError:
    print("Error: Unable to work with the file.")

# Fourth student (Ponomaryova Yana) writes the answer and adds a question
try:
    with open('questions.txt', 'a') as file:
        # Write the student's surname
        file.write('Surname: Ponomaryova\n')
        # Provide the answer
        file.write('Answer: My favorite module is NumPy. It provides powerful capabilities for working with multidimensional arrays and \n')
        file.write('matrices, and includes a large collection of mathematical functions for efficient numerical data processing. \n')
        file.write('NumPy is the foundation for many other libraries, such as Pandas and SciPy, making it an essential tool for\n')
        file.write('scientific computing.\n')
        # Pose a new question for the next student
        file.write('Question: Can you explain how to handle files in Python, including reading and writing?\n')
except IOError:
    print("Error: Unable to work with the file.")

         
        


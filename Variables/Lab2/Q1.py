#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab2/Q1.py
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# ------------------------------------------

"""Lab Description:
Store the following statement in a variable named python_mission.
The mission of the Python Software Foundation is to promote, protect,
and advance the Python programming language, and to support and facilitate
the growth of a diverse and international community of Python programmers
• Count the number of appearances of the letter s.
• Find the second instance of the word Python which occurs somewhere after position 25.
Selection structures and loops should not be used. Your answer should only use string methods.
• What value is returned from the statement
print(“The word returned is: {}”.format(python_mission[25:34]))
• Find out if the word ‘diverse’ is in the mission statement using two different methods
• Check if the string “12345” is a number
• Print out the following directory structure as a string
C:\users\ndarby\python3\python-3.5.1\bin"""


python_mission = """The mission of the Python Software Foundation is to promote, protect, 
and advance the Python programming language, and to support and facilitate 
the growth of a diverse and international community of Python programmers"""

# Count the number of appearances of the letter s.
print(python_mission.count('s'))

# Find the second instance of the word Python which occurs somewhere after position 25.
print(python_mission.index("Python", 25))

# What value is returned from the statement
print("The word returned is: {}".format(python_mission[25:34]))

# Answer - The word returned is:  Software

# Find out if the word ‘diverse’ is in the mission statement using two different methods
print(python_mission.index("diverse"))  # Index is 163
print(python_mission.count("diverse"))  # Number of times word "diverse" exists in python_mission

# Check if the string “12345” is a number
print(any(chr.isdigit() for chr in "12345"))  # Method 1
print(any(map(str.isdigit, "12345")))  # Method 2

# Print out the following directory structure as a string
print("C:\\users\\ndarby\\python3\\python-3.5.1\\bin")

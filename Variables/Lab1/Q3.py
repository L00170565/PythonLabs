#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab1/Q3.py
#
# (C) 2021 Panagiotis Drakos, L00170565
# ------------------------------------------

"""Lab Description: Consider the type of information, and it’s structure for the following items.
You are not asked to code anything here. Just consider the information:"""

# ppsn
print("{}".format("1234567FA"))

# Temp in Degrees
Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5.0/9.0
print("Temperature is: {1} C".format(Fahrenheit, Celsius))

# Average collection of exam grades
print("{:0}".format(round(30+40)/2))

# File path
print("{}".format("/home/dev"))

# Miles travelled per day
print("{:0.3f} Miles".format(50.235))

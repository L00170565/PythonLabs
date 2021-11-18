#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab3/Q1.py
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# Lab Description: Create a tuple of 2 fake student lnumbers. Create a list of 2 modules_subjects names that the
# student takes. For each of the subjects create a dictionary with the student lnumber and the
# grade for that module. See below tables for sample data.
# Modify the code to read in a student Lnumber and using a combination of the above fields print
# the name of the modules they take and the grade they received in each module.
# ------------------------------------------


students = ("L12345", "L54321") # Tuple
modules = ["Java_OOProgramming", "Python_Scripting"] # List
java_grades = {"L12345":40, "L54321":70} # Dictionary for Java modules
python_grades = {"L12345":69, "L54321":58} # Dictionary for Python modules

while True:
    for i in range(2):
        student_ID = int(input("Please enter your Student ID:"))
        print("L{:0>8}".format(student_ID))







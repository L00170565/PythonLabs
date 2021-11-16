#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab2/Q2.py
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# Lab Description: From the python_mission string indicated in the previous question
# find the last instance of the word Python. Use only string methods and variables to
# carry out this task. Do not use loops or selection structures.
# ------------------------------------------

python_mission = """The mission of the Python Software Foundation is to promote, protect, 
and advance the Python programming language, and to support and facilitate 
the growth of a diverse and international community of Python programmers"""

print(python_mission.rindex("Python")) # The last index is 202
print(python_mission.rfind("Python")) # Th last instance is 202







# ------------------------------------------
# Project = PythonLabs
# FileName = Lab2/Q3.py
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# ------------------------------------------

# Lab Description: Given the variable suffix_no with a value of 1122. Build an LYIT student number. The number should
# begin with an L and be followed by 8 digits. Where the suffix_no is less than 8 the string should be
# padded with zero’s to a final size of 8. Use only string methods and variables to carry out this task. Do
# not use loops or selection structures. Modify your answer to take in the suffix_no from the user.

suffix_no = int(input("Please provide your LYIT Num:")) # Get string from user and convert it to int
print("L{:0>8}".format(suffix_no))










# ------------------------------------------
# Project = PythonLabs
# FileName = Lab2/Q1.py
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# ------------------------------------------

# Lab Description: Assume that the following is a single line taken from a *Nix password file.
# Separate out each field into the appropriate variables using the slice operator [].
# rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash
# Repeat the process using the split method

Nix_File = "rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash"

username = Nix_File[0:7]
password = Nix_File[8:9]
user_ID = Nix_File[10:14]
group_ID = Nix_File[15:19]
user_ID_Info = Nix_File[20:31]
home_path = Nix_File[31:46]
command_shell = Nix_File[46:]

print("Username: {}".format(username))
print("Password: {}".format(password))
print("User ID: {}".format(user_ID))
print("Group ID: {}".format(group_ID))
print("User ID Info: {}".format(user_ID_Info))
print("Home Path is: {}".format(home_path))
print("Command executed: {}".format(command_shell))

# Another way of splitting the long string into a list
test_list = Nix_File.split(":", 7) # Short method
print(test_list)




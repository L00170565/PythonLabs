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

print("Username: {}".format(Nix_File[0:7]))
print("Password: {}".format(Nix_File[8:9]))
print("User ID: {}".format(Nix_File[10:14]))
print("Group ID: {}".format(Nix_File[15:19]))
print("User ID Info: {}".format(Nix_File[20:31]))
print("Home Path is: {}".format(Nix_File[31:46]))
print("Command executed: {}".format(Nix_File[46:]))

# Another way of splitting the long string into a list
test_list = Nix_File.split(":", 7) # Maximum amount of elements will output
print(test_list)

# Output: ['rlennon', 'x', '1234', '1001', 'Ruth Lennon', '/users/rlennon', '/bin/bash']




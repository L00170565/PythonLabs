# ------------------------------------------
# Project = PythonLabs
# FileName = Lab2/Q1.py
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# Lab Description: Create a guessing game. Allow the user to input a number. Test to see if their guess is right.
# If it is wrong then ask if they want to guess again. Repeat until they either get the answer the right number
# or until they say no when asked if they wish to retry.
# ------------------------------------------

# Pick a random integer between '1' and '20', inclusive,
# and read guesses from the keyboard until this integer is supplied,
# stating whether each guess is too low, too high, or correct
# The number of tries to guess the correct number is outputted. Repeated
# guesses of the same number do not count as additional tries.

import random
answer = random.randint(1, 20) # random members are generated on the range of 1-20
guesses = []
while True:
    # While the user keeps entering integers will continue to play.
    # If any character is inserted will quit game
        guess = int(input("Please enter your guess [1-20]: "))
        if not guess in guesses:
            guesses.append(guess)
        if guess < answer:
            print(" ", guess, "is too low")
        elif guess > answer:
            print(" ", guess, "is too high")
        else:
            print(" ", guess, "is correct")
            break
        print("Total tries used:", len(guesses)) # number of guesses are counted in the output
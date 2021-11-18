#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab2/Q2.py
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# Lab Description: Read in 5 book titles and values. After each title and value is read
# in display the values and produce a running total of the cost
# BookTitle1 Cost Running Total
# ------------------------------------------

books , prices = [] , [] # Create two empty lists

num_of_books = int(input("How many books:")) # Ask the user input for books Title and price
for i in range(num_of_books): # Iterate through the loop to store book Titles and prices
    book_title = input("Please enter a book Title:")
    books.append(book_title)
    price = float(input("Please enter a price:"))
    prices.append(price)
    i+=1
# print("{0:<30s} {1:6.1}".format(book_title, price))
# print("Sum of books in given list:", sum(prices))
title = "Invoice"
print(title.rjust(30, ' ')) # print format for Invoice
title2 = "Customer: L00170565"
print("{:>35s}".format(title2)) # print format for customer
print(50*"-")
for i in range(len(books)): # iterate through the stored books and prices and printout on screen
    print(f'{books[i]} \t\t\t\t\t\t\t\t€ {prices[i]}')

print(50*"-")
print("Total price: €", sum(prices)) # Calculate the total of all books prices

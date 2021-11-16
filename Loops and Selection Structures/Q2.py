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

# title = "Invoice"
# print(title.rjust(30, ' '))
# title2 = "Customer: L00170565"
# print("{:>35s}".format(title2))
#
# print(50*"^")
# print("< {0:<30s} {1:6.8s}".format("Book Title", "Cost" ))
# print("\n" * 2)
books , prices = [] , []

num_of_books = int(input("How many books:"))
for i in range(num_of_books):
    book_title = input("Please enter a book Title:")
    books.append(book_title)
    price = float(input("Please enter a price:"))
    prices.append(price)
    i+=1
# print("{0:<30s} {1:6.1}".format(book_title, price))
# print("Sum of books in given list:", sum(prices))
title = "Invoice"
print(title.rjust(30, ' '))
title2 = "Customer: L00170565"
print("{:>35s}".format(title2))
print(50*"-")
for i in range(len(books)):
    print(f'{books[i]} \t\t\t\t\t\t\t\t€ {prices[i]}')
# print("{0:<30s} {1:6.5}".format(books[], prices[]))
# print(*books, *prices, sep = "\n")
# print(*prices, sep = "\n")
# print("\n" * 2)
#print(*books, sep = "\n")

    # print(50*"-")

# print("< {0:<30s} {1:6.1}".format("Total", price))
print(50*"-")
print("Total price: €", sum(prices))

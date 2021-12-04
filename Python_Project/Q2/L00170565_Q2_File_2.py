#!/usr/bin/env python3

# ------------------------------------------
# File Name = L00170565_Q2_File_2.py
# Project = Python Project
#
# Author = Panagiotis Drakos, L00170565
# Date = 03/12/21
# Copyright = (C) 2021 Panagiotis Drakos
# ------------------------------------------

# Import the libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define User-Agent and make an HTTP response to the specific URL
# noinspection SpellCheckingInspection
headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

# Step 3: Create an empty list to append with the dictionary
cart_list = []  # A new empty list


def read_page_contents():
    """
    ...
    """
    url = 'https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2499334.m570.l1311&_nkw=dewalt+impact+driver&_sacat=0'
    response = requests.get(url, headers=headers)  # Make a get response to fetch the content
    soup = BeautifulSoup(response.text, 'html.parser')  # Use Python HTML parser

    # print(soup.title.text)
    questions = soup.find_all('div', {'class': 's-item__info clearfix'})  # Find all tags with that instance

    # print(len(questions))

    # Step 2: Transform it to a dictionary to use it to append a list later
    for item in questions:
        question = {
            'title ': item.find('a', {'class': 's-item__link'}).text,  # Find as text all the tags with that instance
            'buy': item.find('span', {'class': 's-item__purchase-options-with-icon'}),
            # Find item that is classified as buy it now
            'watchers': item.find('span', {'class': 's-item__dynamic s-item__additionalItemHotness'}),
            # Find item with tag for watchers
            'rating': item.find('span', {'class': 's-item__reviews-count'}),
            'country': item.find('span', {'class': 's-item__location s-item__itemLocation'})
        }
        cart_list.append(question)
    # print(len(cart))
    print(*cart_list, sep='\n')


if __name__ == "__main__":
    read_page_contents()
    # df = pd.DataFrame(cart_list)  # Need to work on that
    # df.to_excel('test.xlsx')

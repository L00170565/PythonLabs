#!/usr/bin/env python3

# ------------------------------------------
# Project =
# FileName =
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# ------------------------------------------

 # '''Import required libraries: BeautifulSoup, requests and the parser lxml'''

from bs4 import BeautifulSoup
import requests
import pandas

website = "http://192.168.209.138/"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'html.parser') # Python html parser
print(soup.prettify())










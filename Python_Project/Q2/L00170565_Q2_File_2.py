#!/usr/bin/env python3

# ------------------------------------------
# Project =
# FileName =
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# ------------------------------------------

# Import the libraries
import requests
from bs4 import BeautifulSoup

#
# Step 1: Define User-Agent and make an HTTP response to the specific URL
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
url = 'https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2499334.m570.l1311&_nkw=dewalt+impact+driver&_sacat=0'
response = requests.get(url, headers = headers) # Make a get response to fetch the content
soup = BeautifulSoup(response.text, 'html.parser') # Use Python HTML parser

#print(soup.title.text)
questions = soup.find_all('div', {'class': 's-item__info clearfix'}) # Find all tags with that instance

#print(len(questions))

for item in questions:
    title = item.find('a', {'class' : 's-item__link'}).text # Find as text all the tags with that instance
    #print(title)
    url = item.find('a', {'class' : 's-item__link'})['href'] # Find the link of all tags with that instance
    #print(url)
    buy = item.find('span', {'class': 's-item__purchase-options-with-icon'}) #Find item that is classified as buy it now
    #print(buy)
    watchers = item.find('span', {'class': 's-item__dynamic s-item__additionalItemHotness'}) #Find with tag for watchers
    #print(watchers)
    rating = item.find('span', {'class': 's-item__reviews-count'})
    #print(rating)
    country = item.find('span', {'class': 's-item__location s-item__itemLocation'})
    #print(country)











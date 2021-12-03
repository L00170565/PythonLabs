#!/usr/bin/env python3

# ------------------------------------------
# Project =
# FileName =
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# ------------------------------------------

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
# url = 'https://www.lyit.ie/Search-Results?Search=computing'
# url = 'https://en.wikipedia.org/wiki/Korean_War'
url = 'https://stackoverflow.com/questions/tagged/python'
r = requests.get(url, headers=headers)

# print(r.status_code)
soup = BeautifulSoup(r.text, "html.parser")

questions = soup.find_all('div', {'class': 'question-summary'})

# print(len(questions))

for item in questions:
    title = item.find('a', {'class': 'question-hyperlink'}).text
    url = item.find('a', {'class': 'question-hyperlink'})['href']

    print(url)











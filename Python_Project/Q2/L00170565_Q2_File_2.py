#!/usr/bin/env python3

# ------------------------------------------
# Project =
# FileName =
#
# (C) 2021 Panagiotis Drakos, L00170565
#
# ------------------------------------------

 # '''Import required libraries: BeautifulSoup, requests and the html parser'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

def read_Page_Contents():
    """ scrape web page contents"""
    print("Contents of Page")

    #url = urlopen("https://www.lyit.ie/")
    url = urlopen("http://192.168.209.138")
    soup = BeautifulSoup(url, "html.parser") # Python html parser
   # soup = BeautifulSoup(url, features="html5lib")

    titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6']) # Headers to read

    print('List all the header tags:', *titles, sep='\n\n') # Print all the headers and separate them with newline


if __name__ == "__main__":
    read_Page_Contents()










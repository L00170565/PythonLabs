#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab8/Q1.py
#
# (C) 2021 Panagiotis Drakos, L00170565
# Networking Lab exercises and Examples
# Description: This example shows how to read the contents of a page using urllib. The contents of the page are
# large and should be parsed further but this serves as a basic example.
# ------------------------------------------

'''Print the web page contents'''

import urllib.request

def read_Page_Contents():
    """ scrape web page contents"""
    print("Contents of Page")

    url = "http://www.google.ie"

    request2 = urllib.request.urlopen(url)
    request = request2.read()

    print(request)

if __name__ == "__main__":
    read_Page_Contents()







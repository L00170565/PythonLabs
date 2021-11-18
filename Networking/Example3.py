#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab8/Q2.py
#
# (C) 2021 Panagiotis Drakos, L00170565
# Networking Lab exercises and Examples
# Description: This example shows how to find out the external address of a machine.
# ------------------------------------------

'''Print the external IP Address'''

import urllib.request
import  re

def read_IP_Address():
    print("Find external IP Address")

    # service to display from external ip address
    # url = "https://whatismyipaddress.com" #forbidden
    url = "http://checkip.dyndns.org"
    print(url)
    request2 = urllib.request.urlopen(url)
    request = request2.read()
    print(request)

    request = str(request)

    theIP = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',request)

    print("our IP Address is:", theIP)

if __name__ == "__main__":
    read_IP_Address()







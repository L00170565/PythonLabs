#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab8-Part2/Q1.py
#
# (C) 2021 Panagiotis Drakos, L00170565
# Networking Lab exercises and Examples
# Description: This example shows how a list of ip addresses can be validated by separating out the parts of the
# string that represent each octet. We have looked at another way of validating ip addresses in
# another handout via regular expressions.
# ------------------------------------------

# Check reachability of the server
import sys

# Checking each of the 4 octets that make up a valid ip address
def ip_address_valid(list):
    for ip in list:
        ip = ip.rstrip








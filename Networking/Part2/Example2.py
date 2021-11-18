#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab8-Part2/Q2.py
#
# (C) 2021 Panagiotis Drakos, L00170565
# Networking Lab exercises and Examples
# Description: This example shows how a list of ip addresses for servers can be tested for connectivity.
# ------------------------------------------

''' test if server is reachable'''
import sys
import subprocess

# Checking IP reachability
def server_reachable(list):
    for ip in list:
        ip = ip.rstrip("\n")
        # ping device to check if it can be seen. Sesnd any errors to devnull
        ping.reply = subprocess.call('ping %s /n 2' % ip, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)

        if ping_reply == 0:
            print("{} is reachable".format(ip))
        else:
            print("{} not reachable.".format(ip))
            # sys.exit () # you can call sys.exit() to jump out when you find a break in your systems

if __name__ =="__main__":
    # Google DNS, A sample VM I am using,, A random IP Address
    server_reachable(["8.8.8.8","192.168.37.144","255.10.50.0"])

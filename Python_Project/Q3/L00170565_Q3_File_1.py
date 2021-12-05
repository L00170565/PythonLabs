#!/usr/bin/env python3

# ------------------------------------------
# File Name = L00170565_Q3_File_1.py
# Project = Python Project
#
# Author = Panagiotis Drakos, L00170565
# Date = 03/12/21
# Copyright = (C) 2021 Panagiotis Drakos
# ------------------------------------------
""" Description: We have first imported the Paramiko library SSHClient in order to be able to initiate
an SSH session with remote host. For an already known host, host system keys can be loaded,
but in order to be more secure, Paramiko's AutoAddPolicy has been used, and instead of loading the
host keys from the system itself, unknown host keys are used. With that second part configured,
a try-catch block is used and execute the instructions for connection. As an extra level of security
in the script we can ask from the user to type required credentials for the SSH session by importing
library getpass. Script can be run through terminal"""

from paramiko.client import SSHClient, AutoAddPolicy
import getpass


def ssh_connection(ip):

    client = SSHClient()
    # client.load_system_host_keys() # For already known hosts
    client.set_missing_host_key_policy(AutoAddPolicy())  # Use unknown host keys for the script
    try:
        # Get user's credentials to initiate the SSH connection
        client.connect(input("Host: "), port=int(input("Port: ")),
                       username=input("Username: "),
                       password=getpass.getpass(prompt='Password: ', stream=None),
                       look_for_keys=False)
        print("Connected Successfully...")
        client.close()  # close the session
    except Exception:
        print("Failed to connect")
    # finally:
    #     client.close()


ssh_connection("192.168.209.138")

#!/usr/bin/env python3

# ------------------------------------------
# File Name = L00170565_Q4_File_2.py
# Project = Python Project
#
# Author = Panagiotis Drakos, L00170565
# Date = 03/12/21
# Copyright = (C) 2021 Panagiotis Drakos
# ------------------------------------------
from sys import stdout

from paramiko.client import SSHClient, AutoAddPolicy
import getpass
import time
import re
import paramiko


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
        connection = client.invoke_shell()
        connection.send("ifconfig > ifconfig.txt\n")
        time.sleep(2)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Command successfully executed on {}".format(ip))
            vm_output = stdout.readlines()
            with open("ifconfig.txt", "w") as out_file:
                for line in input:
                    out_file.write(line)
        client.close()  # close the session
    except paramiko.AuthenticationException:
        print("Failed to connect")
    # finally:
    #     client.close()


ssh_connection("192.168.209.138")












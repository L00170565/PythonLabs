#!/usr/bin/env python3

# ------------------------------------------
# File Name = L00170565_Q4_File_2.py
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
a try-catch block is used and execute the instructions for connection and remote execution of command nmap
to the remote host. Purpose of this script is to install in ubuntu vm curl, to create a folder including two
sub folders under Desktop path and to print out the last time these folders accessed"""

import time
from sys import stdout

from paramiko.client import SSHClient, AutoAddPolicy
import getpass
import paramiko
import os

path1 = '/home/dev/Desktop/Labs/Lab1'
path2 = '/home/dev/Desktop/Labs/Lab2'
access_time1 = os.path.getatime(path1)
access_time2 = os.path.getatime(path2)

local_time1 = time.ctime(access_time1)
local_time2 = time.ctime(access_time2)


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
        connection.send("sudo ")
        (stdin, stdout, stderr) = client.exec_command("mkdir /home/dev/Desktop/Labs")
        (stdin, stdout, stderr) = client.exec_command("mkdir /home/dev/Desktop/Labs/Lab1")
        (stdin, stdout, stderr) = client.exec_command("mkdir /home/dev/Desktop/Labs/Lab2")
        print("Last access time: ", local_time1)
        print("Last access time: ", local_time2)
        client.close()  # close the session
    except paramiko.AuthenticationException:
        print("Failed to connect")


ssh_connection("192.168.209.138")

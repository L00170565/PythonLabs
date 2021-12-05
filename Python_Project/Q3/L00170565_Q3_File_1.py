#!/usr/bin/env python3

# ------------------------------------------
# File Name = L00170565_Q2_File_1.py
# Project = Python Project
#
# Author = Panagiotis Drakos, L00170565
# Date = 03/12/21
# Copyright = (C) 2021 Panagiotis Drakos
# ------------------------------------------


import paramiko
import time
import re


def ssh_connection(ip):
    try:
        username = 'dev'
        password = 'dev123!'

        print('Connection in progress...')
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n")
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Command successfully executed on vm {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


if __name__ == "__main__":
    ssh_connection("192.168.209.139")

















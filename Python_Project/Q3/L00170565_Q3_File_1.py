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
an SSH session with remote host. As a next step, variables were created to include the required
information for the SSH session. For an already known host, host system keys can be loaded,
but in order to be more secure, Paramiko's AutoAddPolicy has been used, and instead of loading the
host keys from the system itself, unknown host keys are used. With that second part configured,
a try-catch block is used and execute the instructions for connection"""

from paramiko.client import SSHClient, AutoAddPolicy


def ssh_connection(ip):
    user_name = "dev"  # provide username
    user_pass = "dev123!"  # provide user password
    remote_ip = "192.168.209.138"  # provide remote host to connect with ssh
    remote_port = 22

    client = SSHClient()
    # client.load_system_host_keys() # For already known hosts
    client.set_missing_host_key_policy(AutoAddPolicy())  # Use unknown host keys for the script
    try:
        client.connect(remote_ip, port=remote_port,
                       username=user_name,
                       password=user_pass,
                       look_for_keys=False)
        print("Connected Successfully...")
        client.close()  # close the session
    except Exception:
        print("Failed to connect")
    # finally:
    #     client.close()


ssh_connection("192.168.209.138")

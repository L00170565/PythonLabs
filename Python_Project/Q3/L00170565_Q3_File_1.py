#!/usr/bin/env python3

# ------------------------------------------
# File Name = L00170565_Q3_File_1.py
# Project = Python Project
#
# Author = Panagiotis Drakos, L00170565
# Date = 03/12/21
# Copyright = (C) 2021 Panagiotis Drakos
# ------------------------------------------
from paramiko.client import SSHClient, AutoAddPolicy


def ssh_connection(ip):
    user_name = "dev"
    user_pass = "dev123!"
    remote_ip = "192.168.209.138"
    remote_port = 22  # Change this if your SSH port is different

    client = SSHClient()
    # client.load_system_host_keys() # For already known hosts
    client.set_missing_host_key_policy(AutoAddPolicy())  # Use unknown host keys for the script
    try:
        client.connect(remote_ip, port=remote_port,
                       username=user_name,
                       password=user_pass,
                       look_for_keys=False)
        print("Connected Successfully...")
        client.close()
    except Exception:
        print("Failed to connect")
    # finally:
    #     client.close()


ssh_connection("192.168.209.138")

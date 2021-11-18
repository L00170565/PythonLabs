#!/usr/bin/env python3

# ------------------------------------------
# Project = PythonLabs
# FileName = Lab8/Q2.py
#
# (C) 2021 Panagiotis Drakos, L00170565
# Networking Lab exercises and Examples
# Description: This example uses sockets to connect to another device and then run commands in that system. In
# essence it runs a port scan on the system.
# ------------------------------------------

''' #!/usr/bin/env python #include this shebang if running in a *nix environment
'''
''' Sockets code to carry out a port scan '''
''' Modified from: '''

import socket
import subprocess
import sys
from datetime import datetime

def port_scan():
    # Clear the screen. Use clear is running in *nix
    # subprocess.call("cls", shell=True)

    # Ask for input
    remoteServer = input("Enter a remote host to scan:")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning in progress...", remoteServerIP)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors

    try:
        # try 1, 1025 if you have time
        for port in range(79,81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}:   Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculate the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print("Scanning Completed in: ", total)

if __name__ == "__main__":
    port_scan()









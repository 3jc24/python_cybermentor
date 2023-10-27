#!/bin/python3
###########################
# Cyber Mentor full video
###########################
import sys
import socket
from datetime import datetime

# define our target

if len(sys.argv) == 2:
    # translate hostname to ipv4
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print ("Hostname could not be resolved.")
        sys.exit()

else:
    print ("Invalid amount of arguments")
    print ("Syntax: 5_portscanner.py <ip>")

# pretty banner
print ("-"*50)
print ("Scanning target " + target)
print ("Time started: " + str(datetime.now()))
print ("-"*50)

#logic

try:
    for port in range(50,85):
        s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # wait for 1 sec
        result = s.connect_ex ((target, port)) # error indicator
        if result == 0:
            print (f"Port {port} is open.")
        s.close()

except KeyboardInterrupt:
    print ("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print ("Connections could not be stablished.")
    sys.exit()












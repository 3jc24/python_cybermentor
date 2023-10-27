#!/bin/python3
###########################
# Cyber Mentor full video
###########################
import socket

HOST = "127.0.0.1"
PORT = 7777

# AF_INET is ipv4
# SOCK_STREAM is a port
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
s.connect ((HOST, PORT))
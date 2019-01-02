#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with open("./rockyou.txt") as f:
    while True:
        line = f.readline()
        
        try:
            s.connect(("2018shell3.picoctf.com", 35225))
            input = s.recv(1024)
            print input
        except Exception:
            pass
        s.close()
        if not line:
            break
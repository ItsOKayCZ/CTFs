#!/usr/bin/python
from pwn import *

s = remote("192.168.159.130", 20003)

print s.recv(1024)

while(True):
    s.sendline(raw_input())

s.interactive()
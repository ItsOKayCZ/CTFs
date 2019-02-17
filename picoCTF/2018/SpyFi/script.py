#!/usr/bin/python
from pwn import *
import re
import string

context.log_level = "error"

"""
Address:
2018shell3.picoctf.com:31123

Key length: 16

The plaintext:
Agent,
Greetings. My situation report is as follows:
{payload}
My agent identifying code is: {flag}.
Down with the Soviets,
006

"""

byte = 2
length = 16
# Finding the offset
# for i in range(1, 20):
# 	s = remote("2018shell3.picoctf.com", 31123)

# 	s.recvuntil("Please enter your situation report: ")

# 	padding = "B"*i + "A"*length*2
# 	print "[#] Padding: {0}".format(padding)
# 	print "[#] Count: {0}".format(i)
# 	s.sendline(padding)

# 	cipher = re.findall("."*length*byte, s.recvall())

# 	found = False
# 	for i in range(0, len(cipher)):
# 		for j in range(i + 1, len(cipher)):
# 			if(cipher[i] == cipher[j]):
# 				print "----------------------------"
# 				print "Found same block {0} {1}".format(i, j)
# 				print "----------------------------"
# 				found = True

# 		if(found):
# 			break

# 	print "{0}\n".format(" ".join(cipher))

# 	if(found):
# 		break

blockOffset = 11
block = 4
plain = ""
for offset in range(1, 100):

	s = remote("2018shell3.picoctf.com", 31123)
	s.recvuntil("Please enter your situation report: ")

	padding = "B"*blockOffset + "A"*(length - offset) + plain
	s.sendline(padding)

	guess = re.findall("."*length*byte, s.recv(1024))[block]
	print "[#] Padding for block: {0}".format(padding)
	print "[#] Block to bruteforce: {0}\n".format(guess)

	for char in string.printable:

		s = remote("2018shell3.picoctf.com", 31123)
		s.recvuntil("Please enter your situation report: ")

		padding = "B"*blockOffset + "A"*(length - offset) + plain + char
		print "[#] Padding: {0}".format(padding)
		s.sendline(padding)

		cipher = re.findall("."*length*byte, s.recv(1024))[block]
		print "[#] Block: {0} : {1}\n".format(cipher, guess)

		if(cipher == guess):
			plain += char

			print "-------------------------------"
			print "Found matching char: {0}".format(char)
			print "Plaintext: {0}".format(plain)
			print "-------------------------------\n\n"
			break
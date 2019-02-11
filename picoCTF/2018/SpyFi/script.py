#!/usr/bin/python
from pwn import *
import re

context.log_level = "error"

"""
Key length: 16

Same block:
06e360d4261ff32a42cff15e63518ec3

"""

length = 16
# for i in range(1, 20):
# 	s = remote("2018shell3.picoctf.com", 31123)

# 	s.recvuntil("Please enter your situation report: ")

# 	padding = "B"*i + "A"*length*2
# 	print "[#] Padding: {0}".format(padding)
# 	print "[#] Count: {0}".format(i)
# 	s.sendline(padding)

# 	cipher = re.findall("."*length*2, s.recvall())

# 	for i in range(0, len(cipher)):
# 		for j in range(i + 1, len(cipher)):
# 			if(cipher[i] == cipher[j]):
# 				print "----------------------------"
# 				print "Found same block {0} {1}".format(i, j)
# 				print "----------------------------"

# 	print "{0}\n".format(" ".join(cipher))

blockOffset = 11
myBlock = 4

output = ""
while True:

	# Get the current block that i need to decipher
	s = remote("2018shell3.picoctf.com", 31123)
	s.recvuntil("Please enter your situation report: ")

	padding = "B"*blockOffset + "A"*(length - 1)
	s.sendline(padding)

	bruteBlock = re.findall("."*length*2, s.recvall())[myBlock]
	print "[#] Trying to bruteforce: {}".format(bruteBlock)

	for i in range(32, 126):
		s = remote("2018shell3.picoctf.com", 31123)

		s.recvuntil("Please enter your situation report: ")

		padding = "B"*blockOffset + "A"*(length - 1) + chr(i)
		print "[#] Padding: {0}".format(padding)
		print "[#] Same block: {0}".format(bruteBlock)
		s.sendline(padding)

		cipher = re.findall("."*length*2, s.recvall())[myBlock]
		if(cipher == bruteBlock):
			print "--------------------"
			print "Found char: {}".format(chr(i))
			print "--------------------"
			break
		
		print "[#] Bruteforce: {}\n".format(cipher)
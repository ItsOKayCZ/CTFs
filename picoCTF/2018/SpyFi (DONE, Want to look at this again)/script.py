#!/usr/bin/python
import socket
import re

"""
Key length: 16

Matching blocks:
06e360d4261ff32a 42cff15e63518ec3 06e360d4261ff32a 42cff15e63518ec3

Offset: 11
"""

keyLength = 16
offset = 11
for i in range(1, 16):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("2018shell3.picoctf.com", 31123))

	s.recv(1024)
	s.recv(1024)

	padding = "B"*i + "A"*keyLength
	print "[#] Padding: " + padding
	print "[#] Length: {}".format(i)
	s.send(padding + "\n")


	cipher = s.recv(1024)
	cipher = re.findall("."*16, cipher)[6:]
	for i in range(len(cipher)):
		for j in range(i + 1, len(cipher)):
			if(cipher[i] == cipher[j]):
				print "-------------------------------------------------------------------------------"
				print "[!!] Found same block Block 1: {0} Block 2: {1}".format(i, j)
				print "-------------------------------------------------------------------------------"

	cipher = " ".join(cipher)
	print "[#] Ciphertext: \n{0}\n".format(cipher)

	s.close()
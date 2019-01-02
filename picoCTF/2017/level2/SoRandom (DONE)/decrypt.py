import random, string

flag = open("randomFlag.txt", "r").read()
print flag

deFlag = ""

random.seed("random")

for c in flag:

	if c.isupper():
		deFlag += chr((ord(c) - ord('A') - random.randrange(0, 26)) % 26 + ord('A'))

	elif c.islower():
		deFlag += chr((ord(c) - ord('a') - random.randrange(0, 26)) % 26 + ord('a'))

	elif c.isdigit():
		deFlag += chr((ord(c) - ord('0') - random.randrange(0, 10)) % 10 + ord('0'))

	else:
		deFlag += c		

print "[#] Decoded flag: " + deFlag
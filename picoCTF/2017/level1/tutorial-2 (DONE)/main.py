import string
rot13 = string.maketrans( 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm", 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")


file = open("message.txt", "r")

msg = string.translate(file.read(), rot13)
print msg
from PIL import Image

image = Image.open("littleschoolbus.bmp")
width, height = image.size
pixels = image.load()

flag = ""

for x in range(width):
    pixel = pixels[x, height-1]
    for x in range(3)[::-1]: # Read BGR instead of RGB
        flag += bin(pixel[x])[-1]

print "".join(chr(int(flag[i:i+8], 2)) for i in xrange(0, len(flag), 8))
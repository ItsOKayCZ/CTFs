value = []

with open("values.txt", "r") as file:

	for line in file:
		line = line.split("=")[1]
		line.replace("\r\n", "")
		line = line[1:]
		value.append(int(line))

print (value[0]) ** value[1] % value[2]
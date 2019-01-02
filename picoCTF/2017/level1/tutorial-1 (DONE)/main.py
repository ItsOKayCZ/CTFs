with open("contractors.txt") as file:
	
	success = False
	for string in file:
		string = string.split()

		try:
			if(string[0] == "Robin"):
				if(string[2] == "Morris"):
					print "Middle name: " + string[1]
					success = True
					break
		except IndexError:
			print "No Middle name. Skipped"

		if(success):
			break
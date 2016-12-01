def ZeroCounter(target):
        counter = 0
        while True:
                result = target / 5 #Find out how many 5s in target
                if result < 1: #If result is less than 1 then no more 5s so ends
                        return counter
                else:
                        target = result #Updates target (kept float so no rounding problems)
                        counter += int(result) # made interger as can't have .something of a zero
        
while True:#While loop here for ease of use when testing & catch errors
	try:
		n = int(input("Input Integer:"))
		if n < 0: # Checks if input is positive as negative values can also be intergers in python
			print("Must be a positive integer")
		else:   #If input is fine run the program
			print(ZeroCounter(n))
			break
	except ValueError:#If non-interger entered will throw a ValueError & caught here
		print("Must be a positive integer")

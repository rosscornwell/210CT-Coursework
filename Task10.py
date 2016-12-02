import random
#creating a list
inp=[int(i) for i in "123123456712123456789123"]

#This section here is for making a random list for testing
##last=0
##for i in range(3000):
##	r=random.randint(1,5)
##	if random.random()>0.15:
##		r=last+r	
##	inp.append(r)
##	last=r
#I left in the section above if you want to create longer lists	

loc=0
maximum=0
i=0
while i<len(inp):#While 'i' is smaller than length of list
	count=1#Count has to start at 1
	for j in range(i+1,len(inp),1):
		if inp[j]<=inp[j-1]:
                        #if the current value is small than the last
                        #sequence is over
			break
		else:#isn't smaller so count continue
			count+=1
	if count>maximum:#updates the maximum count found if needed
		maximum=count
		loc=i   #new starting location
	if i!=j:
		i=j     #Allows to jump sections of the loop
	else:
		i+=1    #Test the next sequence

print("Starting location of sequence: ",loc," Length of squence: ",maximum)
print(inp[loc:loc+maximum])

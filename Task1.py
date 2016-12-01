#This task randomly shuffles the list given to it

import random

def listRandomise(a):
    b = [] # This will be the new list
    for i in range(len(a)):
        x = random.choice(a) #reason for choice function below
        a.remove(x) #remove the selected value from the old list
        b.append(x) #Add the selected value to the new list
    return b


print("Enter your list of numbers separating the numbers with a comma ','")
newList = [int(x) for x in input('-> ').split(",")]
randomList = listRandomise(newList)
print(randomList)


"""I used the choice function as is easier than using the randint function.
If I didn't use the choice function I would take the length of the list and generate
a random number between the list length using it to select which value in the list to
move to the second list. The choice function is just an easier way to do this."""

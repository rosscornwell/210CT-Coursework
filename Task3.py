import math

def highestSquare(value):
        sqValue = math.sqrt(value)      #Find square root of value
        if sqValue == int(sqValue):     #If sqvalue is a integer then result found
                return value
        else:
                sqValue = math.floor(sqValue)   #Round square root down to whole number
                return math.pow(sqValue,2)      #result to the power of two for square number


while True:     #Loop for error catching
        try:
                value = int(input("Input Integer: "))
                if value <=0:
                        print("Must be a positive integer")
                else:
                        print(int(highestSquare(value)))
                        break #Can be removed for constant looping program
        except ValueError:#if non-integer entered will throw ValueError, caught here
                print("Must be a posistive integer")

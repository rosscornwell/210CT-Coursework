
def is_prime(N, a=3):
	if N == 2:
		prime = True
	elif N <= 1 or N % 2 == 0:
		prime =  False
	elif a * a > N:
		prime = True
	elif N % a == 0:
		prime = False
	else:
		return is_prime(N,a+2)
	return prime


print("This program checks if inputted number is prime")
while True:     #Error catching for strings and float inputs
        try:
                value = int(input("Input Number: "))
                print(is_prime(value))
                break
        except ValueError:
                print("Must input an integer")

#BigO = O(n)

def binSearch(arr,top,low):
	left = 0
	right = int(len(arr))
	#print(arr) # Check what is in the list for error checking
	while left <= right:
		middle = int((left + right)/2)
		if arr[middle] <= top and arr[middle] >= low:
			return True
		elif arr[middle] > top:
			right = middle - 1
		elif arr[middle] < low:
			left = middle + 1
	return False

print('This program is binary search between two values')
#Test list of numbers
lis = []
for i in range(50):
    lis.append(i*2)

while True:
        try:
                top = int(input('Top search number ->'))
                low = int(input('Lowest search number ->'))
                if low > top:
                        print('The top number has to be bigger than the lowest number')
                else:
                        print(binSearch(lis,top,low))
                        break
        except ValueError:
                print('Must enter a whole number')


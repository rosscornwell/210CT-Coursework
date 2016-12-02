#BigO notation = O(n)
def swap(arr):
	wordLen = len(arr)
	if wordLen == 1:        #Checks if only one word left
		return arr
	return [arr[-1]] + swap(arr[:-1])#returns the last word on the list
                                         #recalls the function with all words but the last

arr = input('Enter sentence to reverse: ').split(' ')   #split the sentence by the spaces
arr = swap(arr)
word = ''       #Has to have a starting value defined as a blank string
for i in range(0,len(arr)): word += arr[i] +' ' #Putting it back together again with spaces
print(word)

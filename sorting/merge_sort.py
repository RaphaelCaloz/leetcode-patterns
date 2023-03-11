### START OF TEMPLATE ###
def merge_sort(arr):
	if len(arr) > 1:
		
		# Find mid of array
		mid = len(arr)//2

		# Divide array elements
		L = arr[:mid]
		R = arr[mid:]

		# Sort each half recursively
		merge_sort(L)
		merge_sort(R)

		# Merge sorted halves
		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Merge remaining elements from the half 
		# that has not been fully merged
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
### END OF TEMPLATE ###


# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	merge_sort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)

# This code is contributed by Mayank Khanna

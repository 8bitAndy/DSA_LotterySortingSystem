"""
Written by: Liam Andrews
Student Number: 1054 8022
Question 1 part (f)

This version of counting sort allows for duplicate values
"""

# Initial list of values
A = [41, 10, -16, 15, 7, 43, 0, 11, -16, 2, 0, -1, 39, 43, 10, -16]

# Size of List A, used for later
size = len(A)

# Create output array same size as input array
output = [0] * size


# Loop through A
for i in range(size):

	# Elements smaller than current element
	count = 0

	# Amount of duplicates of an element
	amount = 0

	# Current element i from List A
	currentNum = A[i]

	# Compare every element to current element to see if they are smaller
	for x in range(size):
		# We know we have a duplicate here
		if currentNum == A[x]:
			amount = amount + 1
		# Check if element x is smaller than element i
		elif currentNum > A[x]:
			count = count + 1

	# If there is only a single instance of element do this
	if amount < 1:
		# Insert values into sorted array
		output[count] = currentNum

	# Logic for inserting duplicates 
	else:
		for j in range(amount):
			output[count + j] = currentNum



print()
# Print sorted and unsorted list for comparison
print("Unsorted list:")
print(A)

print("Sorted list:")
print(output)
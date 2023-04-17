"""
Written by: Liam Andrews
Student Number: 1054 8022
Question 1
"""


# Initial list of values
A = [41, 15, 7, 89, 11, 2, -62, -1, 39, 43, 44, 19, 12, 0, 16, 6, -58, 4, 46, 56]

# Size of List A, used for later
size = len(A)



# Create an empty list for the output same size as 
output = [0] * size


# Loop through A
for i in range(size):

	# Elements smaller than current element
	count = 0

	# Current element i from List A
	currentNum = A[i]

	# Compare every element to current element to see if they are smaller
	for x in range(size):
		# Check if element x is smaller than element i
		if currentNum > A[x]:
			count = count + 1

	# Insert values into sorted array
	output[count] = currentNum



# Print sorted and unsorted list for comparison
print()
print("Unsorted list:")
print(A)

print("Sorted list:")
print(output)
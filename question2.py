"""
Written by: Liam Andrews
Student Number: 1054 8022
Question 2
"""

import random
import time
import sys

# Increase memory allocated for recursive functions, prevents errors from happening
sys.setrecursionlimit(10**6)

# Global vars used to count number of comparisons in algorithms
selectionCount = 0
insertionCount = 0
quickCount = 0
mergeCount = 0
countingSort2Count = 0


# Prompts user with main menu, user input determines the flow of program
def mainMenu():

	# Allows for the counting variables to be reset
	global selectionCount
	global insertionCount
	global quickCount
	global mergeCount
	global countingSort2Count

	# User's input for menu below
	menuChoice = 0

	# Loop until the user makes a choice then call appropriate function for choice
	while(menuChoice != 3):
		try:
			selectionCount = 0
			insertionCount = 0
			quickCount = 0
			mergeCount = 0
			countingSort2Count = 0

			print("1. Test an individual sorting algorithm")
			print("2. Test multiple sorting algorithms")
			print("3. Quit program\n")

			menuChoice = int(input("Your choice: "))
			print()

			# Call appropriate function determined by user input, then break out of loop
			if menuChoice == 1:
				singleAlgorithm()
			elif menuChoice == 2:
				multiAlgorithm()

		# Error handling for incorrect user input
		except ValueError:
			print("\nError try again\n")
			continue


# Only does a single algorithm search pattern
def singleAlgorithm():
	print("1. Selection sort")
	print("2. Insertion sort")
	print("3. Merge sort")
	print("4. Quick sort")
	print("5. Counting sort\n")
	

	# Error handling for main menu
	try:
		algoChoice = int(input("Enter your choice of algorithm: "))

		# Sanitise user input so that only correct input is entered
		if algoChoice == 1 or algoChoice == 2 or algoChoice == 3 or algoChoice == 4 or algoChoice == 5:

			# Get the size of the array from the user
			arraySize = int(input("Enter the size of the array n: "))
			print("\n---------------------------------------------\n")

			# Generate an array A[] with n amount of random values
			A = randomArray(arraySize)

		# Error message for wrong user input
		else:
			print("Invalid choice try again\n")
			return
		
		# Invokes function depending on user input from main menu
		if algoChoice == 1:
			start_time = time.perf_counter_ns() / 1000000
			selectionSort(A)
			end_time = time.perf_counter_ns() / 1000000
			execution_time = round((end_time - start_time), 2)

			print("Selection sort:\n")
			print("There were", selectionCount, "comparisons that occurred.")
			print("Runtime was", execution_time, "ms")
			print("There were", arraySize, "elements in the list")

		elif algoChoice == 2:
			start_time = time.perf_counter_ns() / 1000000
			insertionSort(A)
			end_time = time.perf_counter_ns() / 1000000
			execution_time = round((end_time - start_time), 2)

			print("Insertion sort:\n")
			print("There were", insertionCount, "comparisons that occurred.")
			print("Runtime was", execution_time, "ms")
			print("There were", arraySize, "elements in the list")

		elif algoChoice == 3:
			start_time = time.perf_counter_ns() / 1000000
			mergeSort(A)
			end_time = time.perf_counter_ns() / 1000000
			execution_time = round((end_time - start_time), 2)

			print("Merge sort:\n")
			print("There were", mergeCount, "comparisons that occurred.")
			print("Runtime was", execution_time, "ms")
			print("There were", arraySize, "elements in the list")

		elif algoChoice == 4:
			start_time = time.perf_counter_ns() / 1000000
			quickSort(A, 0, (len(A) -1))
			end_time = time.perf_counter_ns() / 1000000
			execution_time = round((end_time - start_time), 2)

			print("Quick sort:\n")
			print("There were", quickCount, "comparisons that occurred.")
			print("Runtime was", execution_time, "ms")
			print("There were", arraySize, "elements in the list")

		elif algoChoice == 5:
			start_time = time.perf_counter_ns() / 1000000
			countingSort2(A)
			end_time = time.perf_counter_ns() / 1000000
			execution_time = round((end_time - start_time), 2)

			print("CountingSort2 sort:\n")
			print("There were", countingSort2Count, "comparisons that occurred.")
			print("Runtime was", execution_time, "ms")
			print("There were", arraySize, "elements in the list")

		# Create blank spaces to help with formatting
		print("\n---------------------------------------------\n")

	except ValueError:
		print("Wrong input try again\n")


# Performs every type of sorting algorithm and compares results
def multiAlgorithm():
	# Get the size of the array from the user
	arraySize = int(input("Enter the size of the array n: "))

	# Prevent any issues from wrong negative inputs, returns back to menu
	if arraySize < 0:
		print("\nError you cannot have an array with a negative length!\n")
		return

	# Generate an array A[] with n amount of random values
	A = randomArray(arraySize)

	# Make duplicates of the list A so that an unsorted list can be passed into some of the functions below
	B = list(A)
	C = list(A)

	#-------------Execute sorting algorithms------------------

	# Get comparisons and runtime of Selection sort
	start_time = time.perf_counter_ns() / 1000000
	selectionSort(A)
	end_time = time.perf_counter_ns() / 1000000
	selectionExecutionTime = str(round((end_time - start_time), 3))  + " (ms.)"

	# Get comparisons and runtime of Insertion sort
	start_time = time.perf_counter_ns() / 1000000
	insertionSort(C)
	end_time = time.perf_counter_ns() / 1000000
	insertionExecutionTime = str(round((end_time - start_time), 3))  + " (ms.)"

	# Get comparisons and runtime of Merge sort
	start_time = time.perf_counter_ns() / 1000000
	mergeSort(A)
	end_time = time.perf_counter_ns() / 1000000
	mergeExecutionTime = str(round((end_time - start_time), 3))  + " (ms.)"

	# Get comparisons and runtime of Quick sort
	start_time = time.perf_counter_ns() / 1000000
	quickSort(B, 0, (len(B) -1))
	end_time = time.perf_counter_ns() / 1000000
	quickExecutionTime = str(round((end_time - start_time), 3)) + " (ms.)"

	# Get comparisons and runtime of Counting sort2
	start_time = time.perf_counter_ns() / 1000000
	countingSort2(A)
	end_time = time.perf_counter_ns() / 1000000
	countingExecutionTime = str(round((end_time - start_time), 3)) + " (ms.)"

	# Print out table of results, formatted so that any size of input doesn't change the look of the table
	print("\n| Sorting algorithm name  | Array size | Num. of Comparisons | Run time (in ms.)")
	print("---------------------------------------------------------------------------------")
	print("{:25s} {:2} {:9} {:9s} {:11s} {:5s} {:5s}".format("| Selection Sort", "|", str(arraySize), "|", str(selectionCount), "|", str(selectionExecutionTime)))
	print("{:25s} {:2} {:9} {:9s} {:11s} {:5s} {:5s}".format("| Insertion Sort", "|", str(arraySize), "|", str(insertionCount), "|", str(insertionExecutionTime)))
	print("{:25s} {:2} {:9} {:9s} {:11s} {:5s} {:5s}".format("| Merge Sort ", 	 "|", str(arraySize), "|", str(mergeCount), 	"|", str(mergeExecutionTime)))
	print("{:25s} {:2} {:9} {:9s} {:11s} {:5s} {:5s}".format("| Quick Sort", 	 "|", str(arraySize), "|", str(quickCount), 	"|", str(quickExecutionTime)))
	print("{:25s} {:2} {:9} {:9s} {:11s} {:5s} {:5s}".format("| Counting Sort2", "|", str(arraySize), "|", str(countingSort2Count), "|", str(countingExecutionTime)))
	print()


# Generate a list of length n with random elements. Input is the intended size of the output array
def randomArray(size):

	# Initialises array with empty values
	array = [0] * size

	# Loop through each index of array and random generate and number for array
	for i in range(size):
		# Random integers can be of any value between -100 to 100 inclusive
		array[i] = random.randint(-100, 100)

	# Return array containing randomly generate values
	return array

"""
The below functions implement the 5 required sorting algorithms for question 2

"""

# Implements a selection sort functionality
def selectionSort(array):
	
	# Counter used to determine the number of comparisons in algorithm
	global selectionCount
	
	# Loop through array
	for i in range(len(array)):

		# Minimum value within the array each loop
		minimum = i

		# Check each element in array against the current minimum
		for x in range(i + 1, len(array)):

			# Determines the current smallest element for our array
			if array[x] < array[minimum]:
				minimum = x

			# Increment number of comparisons for global variable counter
			selectionCount = selectionCount + 1

		# Swap the two elements within the array 
		tempValue = array[minimum]
		array[minimum] = array[i]
		array[i] = tempValue


def insertionSort(array):

	# Counter used to determine the number of comparisons in algorithm
	global insertionCount

	# Loop through array and compare every value to key
	for i in range(1, len(array)):

		# Get the next element to be compared and assign to variable current
		current = array[i]
		x = i - 1

		# Loop through each element and compare to current element
		while x >= 0 and current < array[x]:

			array[x + 1] = array[x]
			x = x - 1

		# Increment number of comparisons
		insertionCount = insertionCount + 1

		# Move sorted value to correct position within array
		array[x + 1] = current


# Recursive sorting algorithm, implements a merge sort algorithm
def mergeSort(array):
	global mergeCount
	# Get the size of the array
	size = len(array)

	# Only do the sort if array is greater than length 1. Continually divide the array into smaller subarrays
	if size > 1:
		mergeCount += 1

		# Get the middle point of array
		r = size // 2

		# Create our two subarrays, sub 1 is the first half, sub 2 is the second half
		sub1 = array[:r]
		sub2 = array[r:]

		# Recursively call the mergesort function upon our subarrays
		mergeSort(sub1)
		mergeSort(sub2)


		#This portion of the function is responsible for merging the subarrays back into a single sorted array

		# Pointers that help with the merge part of the algorithm
		array1ptr = 0
		array2ptr = 0
		mainArrayptr = 0

		# Repeat until we reach the end of one of the subarrays
		while(array1ptr < len(sub1) and array2ptr < len(sub2)):
			if sub1[array1ptr] < sub2[array2ptr]:
				array[mainArrayptr] = sub1[array1ptr]
				array1ptr += 1
			else:
				array[mainArrayptr] = sub2[array2ptr]
				array2ptr += 1
			
			# Increment pointer for main array
			mainArrayptr += 1

			mergeCount += 1
			

		# Repeat until the end of sub array 1 or 2 is reached. Then add all remaining elements into subarray
		while array1ptr < len(sub1):
			array[mainArrayptr] = sub1[array1ptr]
			array1ptr += 1
			mainArrayptr += 1
			mergeCount += 1

		while array2ptr < len(sub2):
			array[mainArrayptr] = sub2[array2ptr]
			array2ptr += 1
			mainArrayptr += 1
			mergeCount += 1

	return array


def quickSort(array, low, high):
	global quickCount

	# Only repeat if the low pointer hasn't reached the high pointer
	if low < high:
		quickCount = quickCount + 1
		pivot = partitionArray(array, low, high)

		# Recursively sort left and right sub arrays
		quickSort(array, low, pivot - 1)

		quickSort(array, pivot + 1, high)

	return array

# Will pick right most element for pivot when making function
def partitionArray(array, low, high):
	# Counter used to determine the number of comparisons in algorithm
	global quickCount

	# Choose a pivot randomly from the array
	pivot = array[high]

	i = low - 1

	for x in range(low,high):

		if array[x] <= pivot:
			i = i + 1
			quickCount = quickCount + 1

			# Swap element at i with element at x
			(array[i], array[x]) = (array[x], array[i])
	
	(array[i + 1], array[high]) = (array[high], array[i + 1])   

	return i + 1

# Implements the counting sort algorithm from part one of the assignment
def countingSort2(array):

	# Counter used to determine the number of comparisons in algorithm
	global countingSort2Count

	# Size of List A, used for later
	size = len(array)

	# Create empty list same size as A, with zero for every value
	C = [0] * size

	# Create an empty array for the output
	output = [0] * size


	# Loop through A
	for i in range(size):

		# Elements smaller than current element
		count = 0

		# Amount of duplicates of an element
		amount = 0

		# Current element i from List A
		currentNum = array[i]

		# Compare every element to current element to see if they are smaller
		for x in range(size):

			# We know we have a duplicate here
			if currentNum == array[x]:
				amount = amount + 1
				countingSort2Count = countingSort2Count + 1
			# Check if element x is smaller than element i
			elif currentNum > array[x]:
				count = count + 1
				countingSort2Count = countingSort2Count + 1

			# Increment number of comparisons
			countingSort2Count = countingSort2Count + 1

		# If there is only a single instance of element do this
		if amount < 1:
			# Insert values into sorted array
			output[count] = currentNum

		# Logic for inserting duplicates 
		else:
			for j in range(amount):
				output[count + j] = currentNum


#-------------Code for part (b)----------------------

# Function prints the amount of average time for a sort and the average amount of comparisons for 10 repetitions
def avgComparisons():

	# Used for counting the number of comparisons that occur within the sorts
	global quickCount
	global mergeCount
	global selectionCount
	global insertionCount
	global countingSort2Count

	
	comparisonList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	timeList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	for i in range(10):
		start_time = time.perf_counter_ns() / 1000000
		A = randomArray(2000)
		mergeCount = 0

		mergeSort(A)

		comparisonList[i] = mergeCount
		end_time = time.perf_counter_ns() / 1000000


		executionTime = round((end_time - start_time), 3)
		timeList[i] = executionTime 

	total = 0
	totalRunTime = 0
	for x in range(10):
		print("\nnum", x, "comparisons this time", comparisonList[x])
		total += comparisonList[x]
		totalRunTime += timeList[x]
		print("time", x, "this loop took", timeList[x])
	
	print("\naverage comparisons were:", (total / 10))
	print("average run time was:", (totalRunTime / 10))
	print("total count", total)
	print("Run time in ms:",totalRunTime)
	print("Input size was:", len(A))



# Main program loop that calls the main menu function
def main():
	mainMenu()

# Run the main loop of the program
main()
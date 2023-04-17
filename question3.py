"""
Written by: Liam Andrews
Student Number: 1054 8022
Question 2
"""

import random

def generateNumbers():

	# List of winning numbers that will be filled later
	WinNo = [0] * 8

	# Generate a list of 8 distinct integers, from values between 1-30
	for i in range(len(WinNo)):

		# Currently drawn winning number
		currentNum = random.randint(1,30)

		# Loop until number is a new distinct number, ensures no repeats
		while currentNum in WinNo:
			# Currently drawn winning number
			currentNum = random.randint(1,30)

		# Add new number to our list of winning numbers
		WinNo[i] = currentNum

	return WinNo


# Generates a list of players and their game-numbers
def generatePlayerList():
	
	# Create player list of 1000 players each with lotto numbers
	lotto = []

	# Create the 2D array and populate it with the players lotto numbers
	for i in range(1000):
		lotto.append([i] * 6)

		# Add 6 numbers to
		for x in range(6):

			# Currently generated number for player, between 1-30 inclusive
			currentNum = random.randint(1,30)

			# Loop until a distinct number is generated for the player
			while currentNum in lotto[i]:
				currentNum = random.randint(1,30)

			# Assign that number to current player give that it is unique
			lotto[i][x] = currentNum


	# Returns the 2D array of players to the calling function
	return lotto


# Used to help sort PWNs, implements a simple insertion sort
def insertionSort(array):


	# Loop through array and compare every value to key
	for i in range(1, len(array)):

		# Get the next element to be compared and assign to variable current
		current = array[i]
		x = i - 1

		# Loop through each element and compare to current element
		while x >= 0 and current < array[x]:

			array[x + 1] = array[x]
			x = x - 1

		# Move sorted value to correct position within array
		array[x + 1] = current

	# Return the sorted array back to the function that called it
	return array


# Used to help sort SWNs, implements a selection sort functionality
def selectionSort(array):
	
	# Loop through array
	for i in range(len(array)):

		# Minimum value within the array each loop
		minimum = i

		# Check each element in array against the current minimum
		for x in range(i + 1, len(array)):

			# Determines the current smallest element for our array
			if array[x] < array[minimum]:
				minimum = x

		# Swap the two elements within the array 
		tempValue = array[minimum]
		array[minimum] = array[i]
		array[i] = tempValue

	return array


# Used to help sort players game-numbers, implements a merge sort algorithm
def mergeSort(array):

	# Get the size of the array
	size = len(array)

	# Only do the sort if array is greater than length 1. Continually divide the array into smaller subarrays
	if size > 1:
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

		# Repeat until the end of sub array 1 or 2 is reached. Then add all remaining elements into subarray
		while array1ptr < len(sub1):
			array[mainArrayptr] = sub1[array1ptr]
			array1ptr += 1
			mainArrayptr += 1

		while array2ptr < len(sub2):
			array[mainArrayptr] = sub2[array2ptr]
			array2ptr += 1
			mainArrayptr += 1

	return array


def preProcessingStage():

	# Loop through the list of players and sort their game-numbers
	insertionSort()


# Fufills system behaviour 1 to show all player's initialized data
def showInitializedData(lotto, WinNo):
	
	# Create table header
	print("\nPlayer's ID | Player's game numbers")
	print("------------------------------------------")

	# Print out every player and their game-numbers
	for i, numbers in enumerate(lotto):
		# Provides proper formatting for output
		print(" {:5} {:4s} {:1} {:15}".format("", str(i), "|", str(numbers)))

	# Empty subarray for PWNs and SWNs to be used below
	PWNs = []
	SWNs = []

	# Get PWNs
	for x in range(6):
		PWNs.append(WinNo[x])

	# Get SWNs
	for y in range(6, 8):
		SWNs.append(WinNo[y])

	# Print out primary and supplementary numbers in a table
	print()
	print(" {:9} {:15s} {:3} {:1}".format("", "PWNs", "|", "SWNs"))
	print("--------------------------------------")
	print(" {:25} {:2s} {:1}".format(str(PWNs), "|", str(SWNs)))


# Fufills task 2 of system functionality, displays the statistics of all winners
def displayStats(lotto, WinNo):

	firstClassWinners = 0
	secondClassWinners = 0
	thirdClassWinners = 0
	fourthClassWinners = 0

	# Get the PWNs and put them in a list
	PWNs = []
	for j in range(6):
		PWNs.append(WinNo[j])

	# Loop through list of players and their game-numbers
	for i in lotto:
		# Number of matching numbers
		matches = 0
		# Check each of the players numbers against the winning numbers
		for x in i:

			# Search and see if x is contained within the PWNs
			# Pointers for binary search
			left = 0
			right = len(PWNs) - 1
			middle = 0

			# Repeat until we reach the end of the search
			while left <= right:

				# Get the middle element of the list
				middle = (left + right) // 2
				
				if PWNs[middle] < x:
					left = middle + 1
				elif PWNs[middle] > x:
					right = middle - 1
				# This means we have found a match and the value is within the PWN list
				else:
					matches += 1
					break

		if matches == 6:
			firstClassWinners += 1
		elif matches == 5:
			secondClassWinners += 1
		elif matches == 4:
			thirdClassWinners += 1
		elif matches == 3:
			fourthClassWinners += 1


	# Get the SWNs and put them in a list
	SWNs = []
	for z in range(6):
		SWNs.append(WinNo[j])

	# Search to see if a player's game numbers contain the Supplementary winning numbers
	# Loop through list of players and their game-numbers
	for i in lotto:
		# Number of matching numbers
		matches = 0
		# Check each of the players numbers against the winning numbers
		for x in i:

			# Search and see if x is contained within the SWNs
			# Pointers for binary search
			left = 0
			right = len(SWNs) - 1
			middle = 0

			# Repeat until we reach the end of the search
			while left <= right:

				# Get the middle element of the list
				middle = (left + right) // 2
				
				if SWNs[middle] < x:
					left = middle + 1
				elif SWNs[middle] > x:
					right = middle - 1
				# This means we have found a match and the value is within the PWN list
				else:
					matches += 1
					break

		# Player is a fourth class winner if they have the two SWNs
		if matches == 2:
			fourthClassWinners += 1

	# Displays table of statistics for winners of lotto
	print()
	print(" {:1} {:15s} {:1} {:1}".format("", "Winner class", "|", "Total number of winners"))
	print("---------------------------------------------")
	print(" {:3} {:13s} {:10} {:1}".format("", "1st class", "|", firstClassWinners))
	print(" {:3} {:13s} {:10} {:1}".format("", "2nd class", "|", secondClassWinners))
	print(" {:3} {:13s} {:10} {:1}".format("", "3rd class", "|", thirdClassWinners))
	print(" {:3} {:13s} {:10} {:1}".format("", "4th class", "|", fourthClassWinners))


# Task 3 of the system requirements, shows a players status and displays an appropriate message
def checkStatus(lotto, WinNo):

	print()
	playerNum = int(input("Enter a played ID to search: "))

	if playerNum < 1 or playerNum > 1000:
		print("\nError no player with that ID\n")
		return

	# Counts how many matches a player has
	count = 0
	suppCount = 0

	# Get the PWNs and put them in a list
	PWNs = []
	for j in range(6):
		PWNs.append(WinNo[j])

	# Search through the players numbers to see if there are any matches
	for i in range(6):
		result = jumpSearch(lotto[playerNum-1], PWNs[i])
		# If they have a matching number then increment counter
		if result == 1:
			count += 1

	# Get the SWNs and put them in a list
	SWNs = []
	for k in range(6,8):
		SWNs.append(WinNo[k])

	# Search through the players numbers to see if there are any matches
	for m in range(2):
		result = jumpSearch(lotto[playerNum-1], SWNs[m])
		# If they have a matching number then increment counter
		if result == 1:
			suppCount += 1

	


	# Determine which type of message should be printed out for player
	if count == 6:
		message = "You win the game, congratulations!"
	elif count == 5:
		message = "You are a 2nd class winner, congratulations!"
	elif count == 4:
		message = "You are a 3rd class winner, congratulations!"
	elif count == 3:
		message = "You are a 4th class winner, congratulations!"
	elif suppCount == 2:
		message = "You are a 4th class winner, congratulations!"
	else:
		message = "You are not a winner. Thanks for playing lotto. Good luck next time!"

	# Displays status of an individual player
	print()
	print("-----------------------------------------------------")
	print(" {:1} {:22s} {:2} {:1}".format("", "Player's ID", "|", playerNum))
	print("-----------------------------------------------------")
	print(" {:1} {:22s} {:2} {:1}".format("", "Player's game-numbers:", "|", str(lotto[playerNum-1])))
	print(" {:1} {:22s} {:2} {:1}".format("", "PWNs:", "|", str(PWNs)))
	print(" {:1} {:22s} {:2} {:1}".format("", "SWNs:", "|", str(SWNs)))
	print(" {:1} {:22s} {:2} {:1}".format("", "Player's status:", "|", message))


# This code implements a jump search algorithm. Returns 1 if element was found otherwise zero is returned
def jumpSearch(array, searchTerm):

	# Get size of our current array
	size = len(array)

	# Determine the length of a jump for the search, get the sqrt of the array length then get the floor of that result
	step = int((size ** (1/2)) // 1)

	previous = 0

	# Try and jump to see where element could be 
	while array[(min(step, size)-1)] < searchTerm:
		previous = step
		step += int((size ** (1/2)) // 1)
		# Element was not within block
		if previous >= size:
			return 0

	# Perform a search within curent block 
	while array[int(previous)] < searchTerm:
		previous += 1
		# Search has exhausted itself and element was not found
		if previous == min(step, size):
			return 0

	# Return 1 if the element is found within the players game-numbers
	if array[int(previous)] == searchTerm:
		return 1


# Menu to control lotto system, get the player list and winning number list as input
def menu(lotto, WinNo):

	# For user input in menu
	userChoice = 0

	# Loop endlessly until user enters a choice
	while userChoice != 4:
		print("\n1. Show Initialized data")
		print("2. Display statistics of winners")
		print("3. Check my lotto status")
		print("4. Exit")
		print()

		userChoice = int(input("Enter your choice: "))

		# Invoke function depending on user input
		if userChoice == 1:
			showInitializedData(lotto, WinNo)
		elif userChoice == 2:
			displayStats(lotto, WinNo)
		elif userChoice == 3:
			checkStatus(lotto, WinNo)
		elif userChoice == 4:
			print("\nClosing Program")
			break
		else:
			print("\nWrong input try again")


def main():

	# -------------------Initialization stage of system-------------------
	# Creates list of players and generates their game-numbers, assigns to list lotto[]
	lotto = generatePlayerList()
	# Create the list of 8 winning numbers and assign to WinNo variable
	WinNo = generateNumbers()
	# prints out the winning number listprint("Winning nums", WinNo)
	
	# -------------------Data pre-processing stage -----------------------
	# Sort the game-numbers for all 1000 players
	for i in lotto:
		i = mergeSort(i)

	# Test to print out lotto list
	#for x in lotto:
		#print(x)


	# Sub arrays for getting the Primary and supplementary winning numbers
	PWNs = []
	SWNs = []

	# Separate the PWNs from the rest of the list
	for i in range(6):
		PWNs.append(WinNo[i])

	# Separate the SWNs from the rest of the list
	for i in range(6,8):
		SWNs.append(WinNo[i])

	# Sort the Primary winning numbers and assign value to list
	PWNs = insertionSort(PWNs)

	# Sort the Supplementary winning numbers and assign value to list
	SWNs = selectionSort(SWNs)

	# Recombine the sorted PWNs and SWNs back into a single list called WinNo[]
	WinNo = PWNs + SWNs

	#print(PWNs)
	#print(SWNs)

	#print(WinNo)


	# Calls the main menu for the system, passes in the lotto list and Winning numbers list
	menu(lotto, WinNo)


main()
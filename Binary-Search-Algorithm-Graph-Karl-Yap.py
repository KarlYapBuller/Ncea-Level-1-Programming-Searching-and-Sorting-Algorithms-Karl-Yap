#Ncea Level 1 Programming Searching and Sorting Algorithms Assessment
#Binary Search algorithim Graph

#Impart random is used for to choose a random number inbetween the ranges of the lists
import random

#List of numbers that are going to be used for the binary search algorithm graph
#The list of numbers has to be sorted in order for binary search to happen
#This list of 20 data values will not be used as we have already found the average cost for this dataset in
#another component
list_20 = [1, 7, 10, 23, 37, 40, 46, 51, 73, 74, 88, 94, 102, 103, 106, 111, 126, 132, 143, 150]
#List of numbers used to find the average cost of increasing the binary search dataset
list_10 = range(1, 10)
list_30 = range(1, 30)
list_40 = range(1, 40)
list_50 = range(1, 50)
list_60 = range(1, 60)
list_70 = range(1, 70)
list_80 = range(1, 80)
list_90 = range(1, 90)
list_100 = range(1, 100)

#Binary search algorithm function
def binary_search(sequence, item):
    #Number of comparisons in the linear search algorithm is set to 0 at the start
    number_of_comparisons = 0
    #Beggining (first) element of the list
    first_element = 0
    #Ending (last) element of the list
    #The length of the sequence is -1 because in Python the first element in the list is position 0
    last_element = len(sequence) - 1

    while first_element <= last_element:
        #The midpoint is equal to the middle position between
        #the beggining index and the rest of the items in the list (sequence)
        #Floor division is used so no remainder is left
        midpoint = first_element + (last_element - first_element) // 2
        #Sequence is used so that the midpoint value will
        #be returned instead of the position of the midpoint in the list
        midpoint_value = sequence[midpoint]
        #Display the midpoint value in the list to the User
        print(f"Midpoint in list: {midpoint_value}")
        #Increase the number of comparisons by 1 through each iteration until
        #the item (User Choice) the User wants to find is found
        number_of_comparisons += 1
        #If the midpoint value is equal to the item value (User Choice) return that midpoint
        if midpoint_value == item:
            #Display the number of comparisons made through
            #each iteration of the linear search algorithm to the User
            print(f"Number of comparisons: {number_of_comparisons}")
            print()
            return midpoint

        #If the item we are looking for is less than the midpoint value which means to the left of the midpoint
        #The last element in the list will now be the element directly to the left of the midpoint
        elif item < midpoint_value:
            last_element = midpoint - 1

        #If the item we are looking for is greater than the midpoint value which means to the right of the midpoint
        #The first element in the list will now be the element directly to the right of the midpoint
        else:
            first_element = midpoint + 1

        #Display the number of comparisons made through
        #each iteration of the linear search algorithm to the User
        print(f"Number of comparisons: {number_of_comparisons}")
        print()

    #Return None if the item is not found in the sequence (list)
    return None

#Display the range of the numbers in the list
print(list_10)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_10)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_10, user_choice)}")

#List 20 is not included in the testing for the averages for the comparison of
#the cost of a binary search algorithm as the number of itms in a dataset increases
#as it the average cost for the list of 20 has be found in another component

#Display the range of the numbers in the list
print()
print(list_30)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_30)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_30, user_choice)}")

#Display the range of the numbers in the list
print()
print(list_40)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_40)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_40, user_choice)}")

#Display the range of the numbers in the list
print()
print(list_50)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_50)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_50, user_choice)}")

#Display the range of the numbers in the list
print()
print(list_60)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_60)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_60, user_choice)}")

#Display the range of the numbers in the list
print()
print(list_70)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_70)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_70, user_choice)}")

#Display the range of the numbers in the list
print()
print(list_80)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_80)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_80, user_choice)}")

#Display the range of the numbers in the list
print()
print(list_90)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_90)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_90, user_choice)}")

#Display the range of the numbers in the list
print()
print(list_100)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_100)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {binary_search(list_100, user_choice)}")


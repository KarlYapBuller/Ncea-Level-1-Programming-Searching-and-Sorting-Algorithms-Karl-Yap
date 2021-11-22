#Ncea Level 1 Searching and Sorting Algorithms Assessment
#Binary Search Graph

#Impart random is used for to choose a random number inbetween the ranges of the lists
import random

#Binary search

#List of numbers that are going to be used for the binary search algorithm
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

def binary_search(sequence, item):
    number_of_comparisons = 0
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        number_of_comparisons += 1
        if midpoint_value == item:
            comparisons = f"Number of comparisons: {number_of_comparisons}"
            print(comparisons)
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None


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


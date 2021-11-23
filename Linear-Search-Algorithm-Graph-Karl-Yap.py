#Ncea Level 1 Searching and Sorting Algorithms Assessment
#Linear Search algorithm Graph

#Impart random is used for to choose a random number inbetween the ranges of the lists
import random

#List of numbers that are going to be used for the linear search algorithm graph
#List of numbers used to find the average cost of increasing the binary search dataset
list_10 = range(1, 10)
list_20 = range(1, 20)
list_30 = range(1, 30)
list_40 = range(1, 40)
list_50 = range(1, 50)
list_60 = range(1, 60)
list_70 = range(1, 70)
list_80 = range(1, 80)
list_90 = range(1, 90)
list_100 = range(1, 100)

#Linear search algorithm function
def linear_search(list, len_of_list, item):
    #Number of comparisons in the linear search algorithm is set to 0 at the start
    number_of_comparisons = 0
    for element in range(0, len_of_list):
        #If the element in the list of numbers is equal to the item (User Choice) the
        #User wants to find from the list return that element
        if (list[element] == item):
            #Increase the number of comparisons by 1
            number_of_comparisons += 1
            #Display the number of comparisons made through
            #each iteration of the linear search algorithm to the User
            print(f"Number of comparisons: {number_of_comparisons}")
            return element
        #Increase the number of comparisons by 1 through each iteration until
        #the item (User Choice) the User wants to find is found
        number_of_comparisons += 1
    #If the element is not equal to the item (User Choice) the User is looking for move on
    #the next element to the right of that element for comparison
    return -1

#Display the range of the numbers in the list
print(list_10)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_10)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_10)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_10, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_20)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_20)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_20)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_20, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_30)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_30)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_30)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_30, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_40)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_40)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_40)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_40, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_50)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_50)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_50)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_50, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_60)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_60)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_60)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_60, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_70)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_70)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_70)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_70, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_80)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_80)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_80)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_80, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_90)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_90)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_90)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_90, len_of_list, item)}")

#Display the range of the numbers in the list
print()
print(list_100)
print()
for i in range(5):
    #Ask user for choice and check it is valid
    user_choice = random.choice(list_100)
    #The element (item) the User wants to find from the items in the list
    item = user_choice
    #Length of list
    len_of_list = len(list_100)
    #The item we are searching for position in array
    print(f"Item searching for: {user_choice}")
    #The Position of the item we are searching for in the array
    #The first item in the array is Position 0, the second item in the array is Position 1
    print(f"Position of item in array: {linear_search(list_100, len_of_list, item)}")

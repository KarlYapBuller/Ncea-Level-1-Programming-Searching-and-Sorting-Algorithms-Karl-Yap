#Ncea Level 1 Searching and Sorting Algorithms Assessment
#Binary Search algorithm

#Choice Checker function
def choice_checker(question, valid_list, error_message):

    valid = False
    while not valid:

        try:
            #Ask user for choice and puts choice in lowercase
            response = int(input(question))

            #If the response is in the list return the response
            if response in valid_list:
                return response

            #If the response is not in the list
            #display an Error message to the User
            else:
                print(error_message)
                continue

        #If the User inputs an invalid value
        #display an Error message to the User
        except ValueError:
            print(error_message)
            continue

#List of numbers
#The list of numbers has to be sorted in order for binary search to happen
list = [1, 7, 10, 23, 37, 40, 46, 51, 73, 74, 88, 94, 102, 103, 106, 111, 126, 132, 143, 150]

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

#Instructions and an Error message for the User to follow
#if they input an invalid value for when they choose an element (item)
#the User wants to find from the items in the list
instructions = "Please choose an item in they list above: "
error_not_in_list = "Sorry! That is not in the list above, try find an item in the list above"

print(list)
print()

#Ask user for choice and check if it is valid
user_choice = choice_checker(instructions, list, error_not_in_list)
print()

#Display the position where the element (item) the User is searching for is located in the list
#The first item in the list is position 0 and the second item in the list is position 1
print(f"Item searching for: {user_choice}")
print()
print(f"Position of item in array: {binary_search(list, user_choice)}")



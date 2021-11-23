#Ncea Level 1 Searching and Sorting Algorithms Assessment
#Linear Search algorithm

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
            return element
        #Increase the number of comparisons by 1 through each iteration until
        #the item (User Choice) the User wants to find is found
        number_of_comparisons += 1
        #Display the number of comparisons made through
        #each iteration of the linear search algorithm to the User
        print(f"Number of comparisons: {number_of_comparisons}")
    #If the element is not equal to the item (User Choice) the User is looking for move on
    #the next element to the right of that element for comparison
    return -1

#Instructions and an Error message for the User to follow
#if they input an invalid value for when they choose an element (item)
#the User wants to find from the items in the list
instructions = "Please choose an item in they list above: "
error_not_in_list = "Sorry! That is not in the list above, try find an item in the list above"

#List used for the linear search algorithm
list = [1 , 3, 5, 4, 7, 9]
#Display the list for the User so they can select an item
print(list)

#Ask user for choice and check if it is valid
user_choice = choice_checker(instructions, list, error_not_in_list)
print()
#The element (item) the User wants to find from the items in the list
item = user_choice
#Length of list
len_of_list = len(list)

#Display the position where the element (item) the User is searching for is located in the list
#The first item in the list is position 0 and the second item in the list is position 1
print(f"Position of item in array: {linear_search(list, len_of_list, item)}")


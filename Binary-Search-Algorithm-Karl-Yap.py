#Ncea Level 1 Searching and Sorting Algorithms Assessment

#Binary search

def choice_checker(question, valid_list, error_message):

    valid = False
    while not valid:

        try:
            #Ask user for choice and puts choice in lowercase
            response = int(input(question))


            if response in valid_list:
                return response

            else:
                print(error_message)
                continue

        except ValueError:
            print(error_message)
            continue

#List of numbers
#The list of numbers has to be sorted in order for binary search to happen
list = [1, 7, 10, 23, 37, 40, 46, 51, 73, 74, 88, 94, 102, 103, 106, 111, 126, 132, 143, 150]

def binary_search(sequence, item):
    number_of_comparisons = 0
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        print(f"Midpoint in list: {midpoint_value}")
        number_of_comparisons += 1
        if midpoint_value == item:
            print(f"Number of comparisons: {number_of_comparisons}")
            print()
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

        print(f"Number of comparisons: {number_of_comparisons}")
        print()

    return None

instructions = "Please choose an item in they list above: "
error_not_in_list = "Sorry! That is not in the list above, try find an item in the list above"

print(list)
print()

#Ask user for choice and check it is valid
user_choice = choice_checker(instructions, list, error_not_in_list)
print()

#The item we are searching for position in array
print(f"Item searching for: {user_choice}")
print()
print(f"Position of item in array: {binary_search(list, user_choice)}")



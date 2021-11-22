#Searching and Sorting Algorithms
#Selection Sort Algorithm

#Selection Sort Function
def selection_sort(list):
    #Number of Comparisons
    number_of_comparisons = 0
    #All the elements present in the list
    length_of_list = range(0, len(list))

    for first_element in length_of_list:
        #Set the minimum value to the first element in the unsorted list
        min_value = first_element
        #Increase the number of comparisons by 1 each time the numbers
        #are compared with eachother and swapped
        number_of_comparisons += 1

        #All the elements on the right of the minimum vlaue (first element)
        for right_of_min_value in range(first_element + 1, len(list)):
            #Go through all the elements in the unsorted part of the array (the right of the minimum value)
            #and if an element is smaller than the minimum value
            #change the minimum value to that element (choose the smaller number
            #if their is two or more numbers smaller than the minimum value)
            if list[right_of_min_value] < list[min_value]:
                min_value = right_of_min_value

            #If an item in the unsorted part of the array is found to be lower than
            #the minimum value than switch the positions of the two elements in the list
            if min_value != first_element:
                list[min_value], list[first_element] = list[first_element], list[min_value]

        #Number of comparisons (swaps) made through
        #each iteration until the list is sorted
        print(f"Number of comparisons: {number_of_comparisons}")

    print()
    #Return the sorted list
    return list

#Unsorted list
list_a = [10, 29, 73, 21, 7, 27, 3]
print(f"Unsorted list: {list_a}")
print()

#The list sorted
print(f"Sorted list: {selection_sort(list_a)}")

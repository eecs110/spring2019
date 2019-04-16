# Complete the following exercises:

# 1. Answer:
def print_third_element(my_list:list):
    '''
    Prints the third element of a list (at index 2)
    Args: 
        my_list(list/tuple): a list or tuple with at least three elements
    '''
    print(my_list[2])

print('\nExercise 1...')
print_third_element(['freshman', 'sophomore', 'junior', 'senior'])
print_third_element([12, 24, 36, 48, 60])
print_third_element(((20, 20), (20, 40), (40, 40), (40, 20)))


# 2. Answer:
def append_element(my_list:list, new_element:any):
    '''
    Appends an element to a list.
    Args: 
        my_list(list): a list
        new_element(any): the element you want to append to the list
    Returns:
        the list with the item appended to it
    '''
    my_list.append(new_element)
    return my_list

print('\nExercise 2...')
print(append_element(['freshman', 'sophomore', 'junior', 'senior'], 'masters\'s student'))
print(append_element(['a', 'b', 'c', 'd'], 'e'))
# use indents to help you read your code:
print(
    append_element(
        [(20, 20), (20, 40), (40, 40)], 
        (40, 20)
    )
)
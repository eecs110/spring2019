'''
Part 1:
In this section write two functions: 
1. get_perimeter: returns the perimeter of a rectangle,
2. get_area: returns the area of a rectangle. 
Both functions should have two required arguments: side_1: float, and side_2: float. 
'''

def get_perimeter(side_1:float, side_2: float):
    return 2 * side_1 + 2 * side_2

def get_area(side_1:float, side_2: float):
    return side_1 * side_2




'''
Part 2:
When you're done with Part 1, modify your get_perimeter and get_area functions
so that they have one required argument (side_1:float), and one optional argument 
(side_2:float) that has a default value of None. Then, if the calling funciton
only passes in one argument, assume that you're calculating  the perimeter and 
area of a square.
'''

def get_perimeter_alt(side_1:float, side_2: float=None):
    if side_2 is None:
        return 4 * side_1
    else:
        return 2 * side_1 + 2 * side_2

def get_area_alt(side_1:float, side_2: float=None):
    if side_2 is None:
        return side_1 ** 2
    else:
        return side_1 * side_2
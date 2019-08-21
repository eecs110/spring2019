import triangles
import rectangles

area_triangle_1 = triangles.get_area(32, 23)
hypotenuse_triangle_1 = triangles.get_hypotenuse(32, 23)
perimeter_triangle_1 = triangles.get_perimeter(32, 23)

# print to screen
print('Area:', area_triangle_1)
print('Hypotenuse:', hypotenuse_triangle_1)
print('Perimeter:', perimeter_triangle_1)

'''
TODO: 
Use the functions in the rectangles module that you just made to calculate
the area of the following rectangles, using as few arguments as possible:
    1. side_1= 44, side_2=10.5
    2. side_1= 44, side_2=44
Print your answers to the screen:
'''

# 1. side_1= 44, side_2=10.5
area_rect_1 = rectangles.get_area(44, 10.5)
perimeter_rect_1 = rectangles.get_perimeter(44, 10.5)
print('Area:', area_rect_1)
print('Perimeter:', perimeter_rect_1)

# 2. side_1= 44, side_2=44
# note that we're only passing in 1 argument here:
area_rect_2 = rectangles.get_area_alt(44)
perimeter_rect_2 = rectangles.get_perimeter_alt(44)
print('Area:', area_rect_2)
print('Perimeter:', perimeter_rect_2)


import utilities
from tkinter import Canvas, Tk

gui = Tk()
gui.title('Bubbles from file')
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()
##################################################################################
# Your code below this line...

# Your job: Modify the code below so that as
# you loop through each line of the file, you:
# 1. Converts the line (a string) into to a tuple of floats
# 2. Appends each tuple to the point_list
# 3. Uses the point_list as an argument to 
#    the canvas.create_polygon function

point_list = []
f = open(utilities.get_file_path('florida.csv'))
for line in f.readlines():
    print(line)

points = [(179.8, 55.2), (221.3, 54.8), (232.9, 79.2)]
canvas.create_polygon(points, fill='#e28894')


# Your code above this line
##################################################################################
canvas.mainloop()
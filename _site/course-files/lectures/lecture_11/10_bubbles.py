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
# 1. create a variable called "center" that 
#    stores the first and second number in the line
#    as a (tuple of ints). 
# 2. Create a variable called "radius" that stores the
#    third number in the line.
# 3. Passes the center and radius variables into the
#    utilities.make_circle function as arguments.


f = open(utilities.get_file_path('bubbles.csv'))
for line in f.readlines():
    print(line)

utilities.make_circle(canvas, (30, 90), 50)
utilities.make_circle(canvas, (300, 490), 10)
utilities.make_circle(canvas, (530, 150), 40)

# Your code above this line
##################################################################################
canvas.mainloop()
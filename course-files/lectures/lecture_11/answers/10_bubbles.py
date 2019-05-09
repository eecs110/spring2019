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

f = open(utilities.get_file_path('bubbles.csv'))
for line in f.readlines():
    line = line.replace('\n', '')
    items = line.split(',')
    x = int(items[0])
    y = int(items[1])
    radius = int(items[2])
    print([x, y, radius])
    utilities.make_circle(canvas, (x, y), radius)

# Your code above this line
##################################################################################
canvas.mainloop()
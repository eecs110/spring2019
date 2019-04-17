from tkinter import Canvas, Tk
import helpers  # means that you are importing all of the functions
                       # in the helpers.py file

# initialize window
gui = Tk()
gui.title('Creature')
screen_width = 700
screen_height = 350
canvas = Canvas(
    gui, width=screen_width, height=screen_height, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ############################## 

# --------------------------------------------------------
# To be completed for Part 1 of Homework
# --------------------------------------------------------
helpers.make_oval(canvas, (100, 100), 100, 'green')
helpers.make_oval(canvas, (200, 200), 50, 'blue')
helpers.make_oval(canvas, (300, 300), 25, 'red')

helpers.make_label(canvas, "FUN!!!", (300, 200))
helpers.make_label(canvas, "Python", (20, 20))
helpers.make_label(canvas, "is", (200, 120))

helpers.make_polygon(
    canvas, 
    [(300, 100), (300, 200), (400, 200), (400, 100)],
    is_smooth=True)
helpers.make_polygon(
    canvas, 
    [(400, 100), (400, 200), (500, 200)],
    is_smooth=False)
helpers.make_polygon(
    canvas, 
    [(200, 200), (200, 300), (300, 200)],
    is_smooth=True)

helpers.make_rectangle(canvas)
helpers.make_arc(canvas)
helpers.make_curvy_line(canvas)
helpers.make_dashed_line(canvas)
helpers.make_solid_line(canvas)

# for convenience:
helpers.make_grid(canvas, screen_width, screen_height)

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()

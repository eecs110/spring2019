from tkinter import Canvas, Tk
import random
from helpers import make_grid, run_test
from creature import make_creature, colors

# initialize window
gui = Tk()
gui.title('Creature')
w = 550
h = 550
c = Canvas(
    gui, width=w, height=h, background='white')
c.pack()

############################ OPTIONAL ##############################
# helper function and event handler:
def make_creature_from_click(event):
    c.delete('grid_line')
    make_creature(
        c,
        (event.x, event.y),
        width=random.randint(80, 200),
        primary_color=colors[random.randint(0, len(colors) - 1)], 
        secondary_color=colors[random.randint(0, len(colors) - 1)]
    )
    make_grid(c, w, h)
c.bind('<Button-1>', make_creature_from_click)  # add event handler
########################### END OPTIONAL ############################

# run test
run_test(c)
make_grid(c, w, h)

c.mainloop()

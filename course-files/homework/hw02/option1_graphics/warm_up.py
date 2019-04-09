from tkinter import Canvas, Tk
import helpers

# initialize window
gui = Tk()
c = Canvas(gui, width=700, height=350, background='white')
c.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

helpers.make_label(c)
helpers.make_oval(c)
helpers.make_polygon(c)
helpers.make_rectangle(c)
helpers.make_arc(c)
helpers.make_curvy_line(c)
helpers.make_dashed_line(c)
helpers.make_solid_line(c)
helpers.make_grid(c, 700, 350)

########################## YOUR CODE ABOVE THIS LINE ############################## 
c.mainloop()
from tkinter import Canvas, Tk
import random

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500, background='#FFFFFF')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

def make_circle(canvas, center, radius, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

for i in range(10):
    make_circle(canvas, (250, 250), 25 + i*25, color=None, outline='black', stroke_width=1)






########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()
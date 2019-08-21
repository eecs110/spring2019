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

for i in range(20):
    x = 250
    y = 250 + i * 5
    r = 2 + i * 2
    make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

for i in range(20):
    x = 250
    y = 250 - i * 5
    r = 2 + i * 2
    make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

for i in range(20):
    x = 250 + i * 5
    y = 250
    r = 2 + i * 2
    make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

for i in range(20):
    x = 250 - i * 5
    y = 250
    r = 2 + i * 2
    make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()
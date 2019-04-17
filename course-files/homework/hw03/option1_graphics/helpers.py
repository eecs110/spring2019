'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
Color Picker: https://coolors.co/
'''

# --------------------------------------------------------
# To be completed for Part 1 of Homework
# --------------------------------------------------------
# Text: Modify for Part 1.2.1.
def make_label(canvas, text, position):
    canvas.create_text(
        position, 
        text=text, 
        font=("Purisa", 32),
        anchor='nw'  # align to "northwest" corner
    )

# Oval: Modify for Part 1.2.2.
def make_oval(canvas, center, radius, color):
    top_left = (center[0] - radius, center[1] - radius)
    bottom_right = (center[0] + radius, center[1] + radius)
    canvas.create_oval(
        [top_left, bottom_right],
        fill=color,
        width=5
    )

# Polygon: Modify for Part 1.2.3.
def make_polygon(canvas, points, is_smooth=True):
    canvas.create_polygon(
        points,
        width=2,
        fill='#BCD39C',
        smooth=is_smooth)




# ---------------------------------------------------------------------
# Other functions / code samples that may be useful to you in some form
# ---------------------------------------------------------------------

# Lines
def make_solid_line(canvas):
    canvas.create_line(
        [
            (10, 0), 
            (210, 100), 
            (420, 0), 
            (630, 100)
        ],  # list of x-y pairs
        width=3)

def make_dashed_line(canvas):
    canvas.create_line(
        [
            (10, 100), 
            (210, 0), 
            (420, 100), 
            (630, 10)
        ], 
        fill="#3D9970", 
        dash=(4, 4), 
        width=3)

# curved:
def make_curvy_line(canvas):
    canvas.create_line(
        [
            (0,   100), 
            (50,  150), 
            (100, 100), 
            (150, 150), 
            (200, 100), 
            (250, 150), 
            (300, 100), 
            (350, 150), 
            (400, 100)
        ], 
        splinesteps=20,
        width=3, 
        smooth=True)

# Rectangle
def make_rectangle(canvas):
    canvas.create_rectangle(
        [
            (500, 25), 
            (650, 75)
        ],
        fill="#3D9970")

# Arc
def make_arc(canvas):
    canvas.create_arc(
        [
            (250, 50), 
            (450, 350)
        ],
        width=5,
        style='arc',
        outline='#0074D9'
    )

def make_grid(c, w, h):
    interval = 100

    # Delete old grid if it exists:
    c.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        c.create_line(0, i, w, i, tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            c.create_oval(
                x - offset, 
                y - offset, 
                x + offset,  
                y + offset, 
                fill='black'
            )
            c.create_text(
                x + offset, 
                y + offset, 
                text="({0}, {1})".format(x, y),
                anchor="nw", 
                font=("Purisa", 8)
            )

'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
Color Picker: https://coolors.co/
Some inspiration:
   * https://www.youtube.com/watch?v=yh_A09CrT68
   * https://www.shutterstock.com/image-vector/cute-animals-cartoon-illustrator-flat-design-247667131
   * https://www.pinterest.com/pin/118782508901992203/
   * https://goo.gl/hKewyL 
'''
from tkinter import Canvas, Tk
from helpers import make_grid       # import the make_grid function (for debugging)

gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


########################
# FUNCTION DEFINITIONS #
########################
def make_oval(canvas: Canvas, center: tuple, radius_x: int, radius_y: int, fill: str='hotpink'):
    '''
    Draws an oval to the canvas, centered at the given center, and with the given radius.
    
    Args: 
        canvas(Canvas): a Canvas object where you want the oval to be drawn.
        center(tuple): a tuple that defines the center point, where the first
            element in the tuple refers to the x-coordinate and the second element
            in the tuple refers to the y-coordinate.
        radius_x(int): an int that specifies the radius of the oval
            in the x-direction.
        radius_y(int): an int that specifies the radius of the oval
            in the y-direction.
        fill(str, optional): a string that represents the color of the circle, 
            defaults to hotpink.
    Returns: 
        Nothing. This function's job is to draw something to the screen. It
        does not return a value.
    '''
    # Exercise 1: currently, this function creates a hard-coded oval with a top-left
    # coordinate of (200, 100), and a bottom-right coordinate of (200, 150). Your job is 
    # to modify the code so that the top-left (x, y) and bottom-right (x, y) coordinates 
    # are calculated based on the radius_x, radius_y and center point specified by the arguments; 
    # and that the fill color is  determined by the fill argument.
    canvas.create_oval(
        [
            (100, 100), 
            (200, 150)
        ],
        fill='hotpink')

def make_circle(canvas: Canvas, center: tuple, radius: int, fill: str='hotpink'):
    '''
    Draws a circle to the canvas, centered at the given center, and with the given radius.
    
    Args: 
        canvas(Canvas): a Canvas object where you want the oval to be drawn.
        center(tuple): a tuple that defines the center point, where the first
            element in the tuple refers to the x-coordinate and the second element
            in the tuple refers to the y-coordinate.
        radius(int): an int that specifies the radius of the circle.
        fill(str, optional): a string that represents the color of the circle, 
            defaults to hotpink.
    Returns: 
        Nothing. This function's job is to draw something to the screen. It
        does not return a value.
    '''
    # Exercise 2: currently, this function creates a hard-coded circle with a top-left
    # coordinate of (300, 100), and a bottom-right coordinate of (400, 200). Your job is 
    # to modify the code so that the top-left (x, y) and bottom-right (x, y) coordinates 
    # are calculated based on the radius and center point specified by arguments; 
    # and that the fill color is  determined by the fill argument.
    # HINT: you may do this by calling the make_oval function that you just made in 
    # Exercise 1.
    canvas.create_oval(
        [
            (300, 100), 
            (400, 200)
        ],
        fill='hotpink')


def make_face(canvas: Canvas, center: tuple, width: int):
    '''
    Draws a face (i.e. a circle) with two eyes (i.e. ovals) to the `canvas`, 
    centered at `center,` and with a face  width of `width`.
    
    Args: 
        canvas(Canvas): a Canvas object where you want the oval to be drawn.
        center(tuple): a tuple that defines the center point, where the first
            element in the tuple refers to the x-coordinate and the second element
            in the tuple refers to the y-coordinate.
        width(int): an int that specifies the width of the face.
    Returns: 
        Nothing. This function's job is to draw something to the screen. It
        does not return a value.
    '''
    # Exercise 3: use the make_circle and make_oval functions that you've just
    # created to draw a face. The face should be a circle, and it should have 2
    # oval eyes. The eyes should scale with the width of the face.
    pass

def make_bullseye(canvas: Canvas, center: tuple, radius: int, distance: int=10):
    '''
    Draws a bullseye of 4 concentric circles to the `canvas`, centered at `center.`
    The smallest  concentric circle has a radius of `radius` (value of the argument), and each 
    additional concentric circle has a radius of `distance` units more that the previous 
    circle. For instance, if `radius`=10 and `distance`=5, then the first circle has a 
    radius of 10, the second a radius of 15, the third 20, and the fourth 25.
    
    Args: 
        canvas(Canvas): a Canvas object where you want the oval to be drawn.
        center(tuple): a tuple that defines the center point, where the first
            element in the tuple refers to the x-coordinate and the second element
            in the tuple refers to the y-coordinate.
        radius(int): an int that specifies the radius of the circle.
        distance(int): a int that represents how far apart each circle should be drawn.
    Returns: 
        Nothing. This function's job is to draw something to the screen. It
        does not return a value.
    '''
    # Exercise 4: use the make_circle function that you just created to draw a bullseye. 
    # Hint: you'll have to draw the biggest circle first, or else your big circle will
    # overwrite and block the smaller circles.
    pass



#####################################
# HOW I WANT TO CALL YOUR FUNCTIONS #
#####################################

# for measuring (optional):
make_grid(canvas, 500, 500)

# Exercise 1: ovals:
print('Exercise 1...')
make_oval(canvas, (100, 100), 25, 40)
make_oval(canvas, (200, 100), 40, 25, fill='navy')
make_oval(canvas, (300, 100), 25, 40, fill='teal')
make_oval(canvas, (400, 100), 40, 25)

# Exercise 2: circles:
print('Exercise 2...')
make_circle(canvas, (100, 200), 25, fill='teal')
make_circle(canvas, (200, 200), 50)
make_circle(canvas, (300, 200), 25, fill='navy')
make_circle(canvas, (400, 200), 50, fill='teal')

# Exercise 3: faces:
print('Exercise 3...')
make_face(canvas, (100, 300), 20)
make_face(canvas, (200, 300), 30)
make_face(canvas, (300, 300), 40)
make_face(canvas, (400, 300), 50)

# Exercise 4: bullseye:
print('Exercise 4...')
make_bullseye(canvas, (100, 400), 5, distance=5)
make_bullseye(canvas, (200, 400), 5, distance=10)
make_bullseye(canvas, (300, 400), 10, distance=5)
make_bullseye(canvas, (400, 400), 20, distance=10)



########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    short = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    short.shape('turtle')
    # Set your turtle's speed using .speed(2)
    short.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    short.color('green')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
   # short.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    #short.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    for i in range(4):
        short.forward(100)
        short.left(90)
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    short.goto(-50,-50)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    short.begin_fill()
    short.circle(100)
    short.end_fill()
    short.goto(-250,-250)
    for i in range(6):
        short.forward(100)
        short.right(360/6)
    short.goto(250,250)
    for i in range(5):
        short.forward(100)
        short.right(360/5)
    short.goto(-250,500/2)
    for i in range(10):
        short.forward(100)
        short.right(360/10)
    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

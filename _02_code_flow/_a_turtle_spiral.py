import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    short = turtle.Turtle()
    # This code sets our shape to a turtle
    short.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    short.speed(5)
    # Set your turtle's color using .color('green')
    short.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(1,51):
        short.color(get_random_color())
        # Set the turtle color to a random color

        # Move the turtle (5*i) pixels. 'i' is the loop variable
        short.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        short.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        short.turtlesize(stretch_len=i, stretch_wid=i)
        short.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

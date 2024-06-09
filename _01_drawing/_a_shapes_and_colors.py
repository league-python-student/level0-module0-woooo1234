import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
thomas = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
thomas.shape('turtle')
# Set your turtle's speed using .speed(2)
thomas.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
thomas.color('green')
thomas.pencolor('blue')
# Move your turtle forward using .forward(100)

# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)

# Now put the forward and left/right code into a for loop to repeat 4 times
thomas.begin_fill()
for i in range(4):
    thomas.forward(100)
    thomas.left(90)

thomas.end_fill()
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
thomas.goto(100,73)
# Have your turtle draw a circle using .circle(radius, steps=30)
thomas.color('blue')
thomas.begin_fill()
thomas.circle(150, steps=30)
thomas.end_fill()
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!
thomas.goto(-100,-35)
thomas.color('yellow')
thomas.begin_fill()
thomas.circle(75,steps=10)
thomas.end_fill()

thomas.goto(100,-35)
thomas.color('purple')
thomas.begin_fill()
thomas.circle(50,steps=6)
thomas.end_fill()


thomas.goto(-60,-50)
thomas.color('black')
thomas.begin_fill()
thomas.circle(75,steps=13)
thomas.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()

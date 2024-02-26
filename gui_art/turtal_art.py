import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Function to create a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Function to draw a square
def draw_square():
    pen.color(random_color())
    for _ in range(4):
        pen.forward(100)
        pen.right(90)

# Draw multiple squares
for _ in range(36):
    draw_square()
    pen.right(10)

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()

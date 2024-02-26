import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Function to create trippy art
def trippy_art():
    # Set random pen color
    r = random.random()
    g = random.random()
    b = random.random()
    pen.color(r, g, b)

    # Draw a spiral
    for _ in range(100):
        pen.forward(100)
        pen.right(91)

# Draw multiple spirals
for _ in range(36):
    trippy_art()
    pen.right(10)

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()

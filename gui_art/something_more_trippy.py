import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest
pen.width(2)  # Set the width of the lines

# Function to draw a trippy pattern
def trippy_pattern(size):
    for _ in range(36):
        pen.color(random.random(), random.random(), random.random())  # Random color
        pen.circle(size)
        pen.left(10)

# Set initial size for the circles
size = 100

# Draw multiple layers of interconnected circles
for _ in range(10):
    trippy_pattern(size)
    size += 20  # Increase size for the next layer

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()

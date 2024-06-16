from turtle import *
from random import randint, choice
import math, time

# Initialize and setup
myPen = Turtle()
myPen.shape("turtle")
myPen.speed(0)

window = Screen()
window.title("EID MUBARAK")
window.setup(width=800, height=600)
window.bgcolor("#0b3d91")

# Methods
def draw_circle(paint, color, x, y, radius):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x, y-radius)
    paint.pendown()
    paint.begin_fill()
    paint.circle(radius)
    paint.end_fill()

def draw_star(paint, color, x, y, size):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x, y)
    paint.pendown()
    paint.begin_fill()
    for i in range(5):
        paint.forward(size)
        paint.right(144)
        paint.forward(size)
        paint.left(72)
    paint.end_fill()
    paint.setheading(0)

def draw_rectangle(paint, color, x, y, width, height):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x, y)
    paint.pendown()
    paint.begin_fill()
    for i in range(2):
        paint.forward(width)
        paint.left(90)
        paint.forward(height)
        paint.left(90)
    paint.end_fill()
    paint.setheading(0)

def draw_trapezium(paint, color, x, y, width, height, style):
    rad = 20 * (math.pi / 180)
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x, y)
    paint.pendown()
    paint.begin_fill()
    if style == "normal":
        nor = 1
        rev = 0
    elif style == "reverse":
        nor = 0
        rev = 1
    paint.forward(width - rev * (2 * height * math.sin(rad)))  # parallel side
    paint.left(90 + (20 * nor) - (20 * rev))
    paint.forward(height)
    paint.left(90 - (20 * nor) + (20 * rev))
    paint.forward(width - nor * (2 * height * math.sin(rad)))  # parallel side
    paint.left(90 - (20 * nor) + (20 * rev))
    paint.forward(height)
    paint.left(110 + (20 * nor) - (20 * rev))
    paint.end_fill()
    paint.setheading(0)

# Draw a detailed mosque with domes and minarets
def draw_detailed_mosque(paint, x, y):
    # Base structure
    draw_rectangle(paint, "#B0E0E6", x, y, 300, 150)
    
    # Main dome
    draw_circle(paint, "#FFD700", x + 150, y + 150, 75)
    
    # Smaller domes
    for i in range(2):
        draw_circle(paint, "#FFD700", x + 75 + i*150, y + 100, 50)
    
    # Main entrance
    draw_rectangle(paint, "#FFD700", x + 125, y, 50, 100)
    draw_circle(paint, "#FFD700", x + 150, y + 100, 25)
    
    # Arched windows
    for i in range(3):
        draw_rectangle(paint, "#B0E0E6", x + 25 + i*100, y + 50, 50, 75)
        draw_circle(paint, "#FFD700", x + 50 + i*100, y + 125, 25)
    
    # Minarets
    for i in range(2):
        draw_rectangle(paint, "#B0E0E6", x - 30 + i*360, y, 30, 200)
        draw_circle(paint, "#FFD700", x - 15 + i*360, y + 200, 15)
        paint.penup()
        paint.goto(x - 15 + i*360, y + 215)
        paint.pendown()
        paint.goto(x - 5 + i*360, y + 230)
        paint.goto(x - 25 + i*360, y + 230)
        paint.goto(x - 15 + i*360, y + 215)

# Draw a minar
def draw_minar(paint, color, x, y):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x, y)
    paint.pendown()
    paint.begin_fill()
    # First turn
    paint.forward(60)
    paint.left(90)
    paint.forward(40)
    paint.left(45)
    paint.forward(35)
    paint.right(45)
    paint.forward(30)
    paint.left(45)
    paint.forward(7.42)
    # Second turn
    paint.left(90)
    paint.forward(7.42)  # from Pythagorean theorem
    paint.left(45)
    paint.forward(30)
    paint.right(45)
    paint.forward(35)
    paint.left(45)
    paint.forward(40)
    paint.end_fill()
    paint.setheading(0)

# Function to draw the rest of the scene
def draw_scene():
    # Draw the stars with realistic colors
    star_colors = ["white", "#FFFFE0", "#FFD700", "#B0E0E6"]
    for i in range(25):
        x = randint(-390, 390)
        y = randint(-90, 300)
        size = randint(5, 10)
        color = choice(star_colors)
        draw_star(myPen, color, x, y, size)
    
    # Draw the mosque
    draw_detailed_mosque(myPen, -300, -200)
    draw_rectangle(myPen, "#ffdf00", 250, -280, 50, 8)
    draw_trapezium(myPen, "white", 245, -265, 60, 12, "normal")
    draw_rectangle(myPen, "#ffa500", 250, -245, 10, 70)
    draw_rectangle(myPen, "#ffc500", 267, -245, 16, 70)
    draw_rectangle(myPen, "#ffe500", 290, -245, 10, 70)
    draw_trapezium(myPen, "white", 250, -168, 60, 12, "reverse")
    draw_rectangle(myPen, "white", 233, -145, 10, 20)
    draw_rectangle(myPen, "white", 245, -145, 60, 20)
    draw_rectangle(myPen, "white", 307, -145, 10, 20)
    draw_trapezium(myPen, "#ffa500", 238, -115, 75, 18, "normal")
    draw_rectangle(myPen, "#ffd100", 245, -90, 60, 15)
    draw_minar(myPen, "#6799ff", 245, -65)

    # Draw the moon
    draw_circle(myPen, "white", 210, -10, 30)
    draw_circle(myPen, "#0B3DE7", 203, -3, 30)
    
    # Time for text printing
    myPen.penup()
    myPen.color("gold")
    animate_text()

# Function to animate the "EID MUBARAK" text with colors and movements
def animate_text():
    colors = ["#FFD700", "#FF4500", "#00FF00", "#00BFFF", "#8A2BE2", "#FF1493"]
    message = "EID MUBARAK"
    y_offset = -240

    for i in range(len(message)):
        for j in range(3):
            myPen.goto(-100 + i*30, y_offset + j*10)
            myPen.color(colors[j % len(colors)])
            myPen.write(message[i], align="center", font=("Gabriola", 38, "bold italic"))
            time.sleep(0.05)
            myPen.undo()
        
        myPen.goto(-100 + i*30, y_offset)
        myPen.color(colors[i % len(colors)])
        myPen.write(message[i], align="center", font=("Gabriola", 38, "bold italic"))

    myPen.goto(-350, -260)
    myPen.color("#FFFFFF")  # White color for the message below
    myPen.write("May the blessings of Allah fill your life with happiness and success", align="left",
                font=("Arial", 12, "italic"))
    myPen.goto(-230, -320)
    myPen.write("@Presented By: Basharul Alam Mazu", align="left", font=("Arial", 10, "normal"))

# Function to create a gradient background
def draw_gradient():
    gradient_pen = Turtle()
    gradient_pen.speed(0)
    gradient_pen.penup()
    gradient_pen.hideturtle()
    window.tracer(0)
    
    for i in range(400):
        color = (11 / 255, 61 / 255, 145 / 255 + (110 / 255) * (i / 400))
        gradient_pen.color(color)
        gradient_pen.goto(-400, 300 - i)
        gradient_pen.pendown()
        gradient_pen.begin_fill()
        gradient_pen.goto(400, 300 - i)
        gradient_pen.goto(400, 299 - i)
        gradient_pen.goto(-400, 299 - i)
        gradient_pen.goto(-400, 300 - i)
        gradient_pen.end_fill()
        gradient_pen.penup()
    
    window.tracer(1)

# Draw the gradient background
draw_gradient()

# Start drawing the scene after a short delay
window.ontimer(draw_scene, 1000)

window.mainloop()


import turtle
import random

window = turtle.Screen()
window.title("Catch the Turtle")
window.bgcolor("#33F9FF")
window.setup(width=800, height=600)

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.penup()
turtle_instance.speed(1) 
turtle_instance.goto(0, 0)

def move_turtle():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    turtle_instance.goto(x, y)

def catch(x, y):
    if turtle_instance.distance(x, y) < 20:
        move_turtle()
        update_score()

def update_score():
    global score
    score += 1
    pen.clear()
    pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

window.listen()
window.onscreenclick(catch)

while True:
    move_turtle()
    window.update() 
import turtle
import random
import time
delay = 6
score = 0
bodies = []
s = turtle.Screen()
s.title('Snake game')
s.bgcolor("#758551")
s.setup(width=600,height = 600)
head = turtle.Turtle()
head.speed(10)
head.shape("square")
head.color("black")
head.fillcolor("#856ff8")
head.penup()
head.goto(0,0)
head.direction = "stop"
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.fillcolor("#a88332")
food.penup()
food.ht()
food.goto(0,200)
food.st()
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("press any key to play",font=("courier",40, "normal"))
def moveup():
    if head.direction != "down":
        head.direction = "up"
def movedown():
    if head.direction != "up":
        head.direction = "down"
def moveright():
    if head.direction != "left":
        head.direction = "right"
def moveleft():
    if head.direction != "right":
        head.direction = "left"
def movestop():
    head.direction = "stop"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")
while True:
    s.update()
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    if head.distance(food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        body  = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("black")
        body.fillcolor("black")
        bodies.append(body)
        score += 1
        sb.clear()
        sb.write("Score : "+ str(score),font=("courier",40, "normal"))
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
    for body in bodies:
        if body.distance(head)<10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            score = 0
            sb.clear()
            sb.write("Score : ()",font=("courier",40, "normal"))
s.mainloop()

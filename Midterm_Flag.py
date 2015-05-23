import turtle

def bgr(t):
    t.color("red")
    t.up()
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.down()
    t.begin_fill()
    for i in range(2):
        t.left(90)
        t.forward(600)
        t.left(90)
        t.forward(400)
    t.end_fill()

def sunray(t):
    t.color("black")
    t.begin_fill()
    for i in range(3):
        t.forward(10)
        t.right(4)
    for i in range(3):
        t.forward(10)
        t.left(3)
    t.right(166)
    for i in range(3):
        t.forward(10)
        t.right(4)
    for i in range(3):
        t.forward(10)
        t.left(5)
    t.end_fill()

def sun(t):
    t.goto(0, 80)
    for i in range(40):
        sunray(t)
        t.left(70)
        t.forward(1)
        t.left(87)
    t.up()

def yellowcircle(t):
    t.goto(3, 70)
    t.right(90)
    t.down()
    t.color("yellow")
    t.begin_fill()
    for i in range(90):
        t.forward(4.75)
        t.right(4)
    t.end_fill()
    t.up()

def stripe1(t):
    t.right(168)
    t.down()
    t.color("red")
    t.begin_fill()
    for i in range(33):
        t.forward(5)
        t.left(2)
    t.right(90)
    t.forward(5)
    t.right(90)
    for i in range(33):
        t.forward(5)
        t.right(2)
    t.end_fill()

def stripe2(t):
    t.right(30)
    t.down()
    t.color("red")
    t.begin_fill()
    for i in range(33):
        t.forward(5)
        t.right(2)
    t.left(90)
    t.forward(5)
    t.left(90)
    for i in range(33):
        t.forward(5)
        t.left(2)
    t.end_fill()
    

def main():
    jily = turtle.Turtle()
    wn = turtle.Screen()
    jily.speed(0)
    turtle.setup(600, 400)

    bgr(jily)
    sun(jily)
    yellowcircle(jily)
    
    jily.up()
    jily.goto(50, 55)
    jily.down()
    stripe1(jily)
    
    jily.up()
    jily.goto(60, 48)
    jily.right(10)
    jily.down()
    stripe1(jily)
    
    jily.up()
    jily.goto(70, 40)
    jily.right(10)
    jily.down()
    stripe1(jily)

    jily.up()
    jily.goto(-47, 55)
    jily.left(7)
    jily.down()
    stripe2(jily)
    
    jily.up()
    jily.goto(-57, 48)
    jily.left(208)
    jily.down()
    stripe2(jily)

    jily.up()
    jily.goto(-67, 40)
    jily.left(208)
    jily.down()
    stripe2(jily)

main()
    
    

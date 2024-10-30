import turtle as t
t.speed(0)

def circlea(x,y,r,h):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("white","white")
    t.circle(r,h)
    t.end_fill()

def circleb(x,y,r,h):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("red","red")
    t.circle(r,h)
    t.end_fill()

def circlec(x,y,r,h):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("blue","blue")
    t.circle(r,h)
    t.end_fill()

def star(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("white","white")
    t.seth(0)
    t.fd(160)
    t.right(144)
    t.fd(160)
    t.right(144)
    t.fd(160)
    t.right(144)
    t.fd(160)
    t.right(144)
    t.fd(160)
    t.end_fill()
    t.hideturtle()

def circle_big(x,y,r,h):
    t.seth(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("black","yellow")
    t.circle(r,h)
    t.end_fill()

def circle_small1(x,y,r,h):
    t.seth(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("black","black")
    t.circle(r,h)
    t.end_fill()
    
def circle_small2(x,y,r,h):
    t.seth(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("black","white")
    t.circle(r,h)
    t.end_fill()

def circle(a,x,y,r,h):
    t.seth(a)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r,h)
    t.hideturtle()

    

circleb(-150,-180,180,360)
circlea(-150,-150,150,360)
circleb(-150,-120,120,360)
circlec(-150,-90,90,360)
star(-225,22)


#=================================
t.seth(0)
circleb(200,-180,180,360)
circlea(200,-150,150,360)
circleb(200,-120,120,360)
circlec(200,-90,90,360)
circle_big(200,-90,90,360)
circle_small2(150,20,20,360)
circle_small2(250,20,20,360)
circle_small1(150,20,15,360)
circle_small1(250,20,15,360)
circle(-30,140,-50,120,60)



import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Narodeninová torta")
t = turtle.Turtle()
t.speed(20)

# TORTA
def nakresli_vrstvu(x, y, sirka, vyska, farba):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(farba)
    t.begin_fill()
    for _ in range(2):
        t.forward(sirka)
        t.left(90)
        t.forward(vyska)
        t.left(90)
    t.end_fill()

nakresli_vrstvu(-170, -200, 320, 60, "sienna")
nakresli_vrstvu(-155, -130, 290, 50, "ivory")
nakresli_vrstvu(-142, -72, 264, 45, "lightcoral")

# SVIEČKY
for i in range(8):
    x = -142 + (i + 0.5) * 33
    
    t.penup()
    t.goto(x, -27)
    t.setheading(0)
    t.pendown()
    t.color("lemonchiffon")
    t.pensize(2)
    t.begin_fill()
    t.forward(5)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(25)
    t.end_fill()
    
    t.penup()
    t.goto(x+2.5, -2)
    t.setheading(0)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.pensize(3)

# KONFETY
konfety_x = [-220, -190, -160, -100, -40, 30, 90, 140, 200, 250]
konfety_y = [-10, 20, 40, 30, 50, 30, 10, -10, -30, 0]
farby = ["red","lime","purple","gold","blue","magenta","cyan","orange","pink","yellow"]

for i in range(9):
    t.penup()
    t.goto(konfety_x[i], konfety_y[i])
    t.pendown()
    t.color(farby[i])
    t.begin_fill()
    t.circle(6)
    t.end_fill()
# TEXT
t.penup()
t.goto(-300, 100)
t.color("gold")  
t.write("VŠETKO NAJLEPŠIE K TVOJM NARODENINÁM!", 
        font=("Arial", 18, "bold"))

t.hideturtle()
screen.exitonclick()
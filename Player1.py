import turtle
window = turtle.Screen()
window.title("ping pong Game By SaberHosny")
window.setup(width=800, height=600)
window.tracer(0)
window.bgcolor(.10,.8,.8)


# setup game objects ========
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.goto(x=0,y=0)
ball.penup()

# center line

center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_wid=25,stretch_len=.1)
center_line.penup()
center_line.goto(0,0)

# player1

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1,stretch_wid=5)
player1.color("blue")
player1.penup()
player1.goto(x=-350,y=0)




#player2

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1,stretch_wid=5)
player2.color("red")
player2.penup()
player2.goto(350,0)


# score text

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0,260)
score.write("Payer1:  0 Player2:  0", align="center", font = ("center", 14 ,"normal") )
score.hideturtle()

# game loop ================
while True:
    window.update()





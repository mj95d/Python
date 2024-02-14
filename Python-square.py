import turtle
import time
import random

delay = 0.1

# إعداد النافذة
wn = turtle.Screen()
wn.title("لعبة الثعبان")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# رأس الثعبان
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("Blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# الطعام
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# الدالة الحركية
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# التحكم باللعبة
wn.listen()
wn.onkeypress(go_up, "2")
wn.onkeypress(go_down, "9")
wn.onkeypress(go_left, "1")
wn.onkeypress(go_right, "0")

# الحلقة الرئيسية للعبة
while True:
    wn.update()

    # التصادم مع الحواف
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

    # التصادم مع الطعام
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # حركة الأجزاء الأخيرة
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # حركة الجزء الأول
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # التصادم مع الجسم
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)

wn.mainloop()

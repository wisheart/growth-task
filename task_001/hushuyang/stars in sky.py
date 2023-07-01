import turtle as t


# 画星星
def star(x, y, angle, length):
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.penup()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    for i in range(0, 5):
        t.forward(length)
        t.right(144)
    t.end_fill()  # 填充完成
    # 将画笔方向恢复为水平方向，以免影响后续画图
    t.left(angle)


t.screensize(800, 600, "blue")
t.pensize(4)
t.speed(5)
star(20, 50, 50, 50)
star(70, 100, 100, 100)
star(70, 70, 70, 70)
star(10, 80, 10, 20)
t.end_fill()
t.hideturtle()
t.done()

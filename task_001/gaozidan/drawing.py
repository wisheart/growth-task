from turtle import *
speed(10)
pensize(3)
hideturtle()
screensize(500,500,bg='white')
#猫脸
fillcolor('#048db1')#头的颜色
begin_fill()
circle(150)
end_fill()
pensize(2)
fillcolor('#eff1e3')#脸的颜色
begin_fill()
circle(130)
end_fill()
#围巾
pu()
goto(-70,12)
pensize(14)
color('#c43d44')
pd()
seth(-20)
circle(200,30)
circle(200,10)
#铃铛
pu()
goto(0,-46)
pd()
pensize(1)
color("black",'#ffdf4e')
begin_fill()
circle(25)
end_fill()
pu()
goto(-5,-40)
pd()
pensize(1)
color("black",'#79675d')
begin_fill()
circle(5)
end_fill()
pensize(1)
right(115)
forward(7)
#眼睛
pu()
goto(0,250)
pd()
pensize(2)
color('black','white')
begin_fill()
for i in range(30):
    forward(7.5)
    right(12)
end_fill()
pd()
pensize(2)
color('black','white')
begin_fill()
for i in range(30):
    forward(7.5)
    left(12)
end_fill()
pu()
goto(-15,250)
pd()
pensize(12)
color('black')
for i in range(30):
    forward(2)
    right(12)
pu()
goto(15,250)
pd()
pensize(12)
color('black')
for i in range(30):
    forward(2)
    left(12)
#鼻子
pu()
goto(-25,210)
pd()
pensize(2)
color('black','red')
begin_fill()
circle(20)
end_fill()
pu()
goto(1,215)
pd()
pensize(10)
color('white','white')
begin_fill()
circle(0.6)
end_fill()
pu()
pensize(2)
color('black')
goto(-4,187)
pd()
for k in range(-100,-80):
    k += 0.5
    fd(6)
    seth(k)
pu()
#嘴
goto(-35,50)
pd()
pensize(1)
color('black','red')
begin_fill()
circle(30)
end_fill()
pu()
goto(15,65)
pd()
color('black')
pensize(16.3)
for k in range(-230,-80):
      k -= 0.6
      fd(0.4)
      seth(k)
seth(23)
fd(40)
pu()
goto(18,55)
pd()
color('red')
pensize(12)
for k in range(-190,-120):
      k -= 0.8
      fd(0.7)
      seth(k)
#腮红
pu()
goto(-100,200)
pd()
pensize(1)
color('#eff1e3','pink')
begin_fill()
circle(20)
end_fill()
pu()
goto(65,200)
pd()
pensize(1)
color('#eff1e3','pink')
begin_fill()
circle(20)
end_fill()
#胡须
pu()
goto(-35,170)
pd()
pensize(1)
color('black')
seth(160)
fd(70)
pu()
goto(-40,150)
pd()
pensize(1)
color('black')
seth(180)
fd(75)
pu()
goto(-35,130)
pd()
pensize(1)
color('black')
seth(200)
fd(75)
pu()
goto(35,170)
pd()
pensize(1)
color('black')
seth(20)
fd(70)
pu()
goto(40,145)
pd()
pensize(1)
color('black')
seth(5)
fd(75)
pu()
goto(45,120)
pd()
pensize(1)
color('black')
seth(-15)
fd(75)
done()
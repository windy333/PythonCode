'''
游戏规则: w, s控制PlayerA移动, uparrow, downarrow控制PlayerB移动
P暂停
率先获得10分获胜,获胜后按R重新开始

重要：由于turtle库onkey语句限制两名玩家不能同时操控，还请各位见谅
'''
import turtle as t
from math import *


def bg():
    t.speed(7)
    t.width(10)
    t.up()
    t.goto(400, 300)
    t.setheading(0)
    t.down()
    t.lt(180)
    t.fd(800)
    t.lt(90)
    t.fd(600)
    t.lt(90)
    t.fd(800)
    t.lt(90)
    t.fd(600)
    t.up()
    t.goto(0, 300)
    t.width(4)
    t.lt(180)
    for i in range(40):
        t.down()
        t.fd(5)
        t.up()
        t.fd(10)
    '''
    t.up()
    t.goto(0,320)
    t.down()
    t.write("'P' to pause.",align="center",font=("Arial",15,"normal"))
    t.up()
    '''


def playerA(a):
    t.width(30)
    t.up()
    t.goto(370, a)
    t.down()
    t.setheading(90)
    t.fd(100)


def playerB(a):
    t.width(30)
    t.up()
    t.goto(-370, a)
    t.down()
    t.setheading(90)
    t.fd(100)


def ball(a, b):
    t.up()
    t.goto(a, b)
    t.dot(30)


class dir:
    def x(a): return cos(a) * speed

    def y(a): return sin(a) * speed


def clamp(maxa, mina, a):
    return max(mina, min(maxa, a))


def moveA(a):
    global ha, p
    if (p): return
    ha += a * 10
    ha = clamp(180, -280, ha)


def moveB(a):
    global hb, p
    if (p): return
    hb += a * 10
    hb = clamp(180, -280, hb)


def score(a, b):
    t.up()
    t.goto(-150, 250)
    t.write(str(a), align="center", font=("Arial", 25, "normal"))
    t.goto(150, 250)
    t.write(str(b), align="center", font=("Arial", 25, "normal"))
    t.up()


def pause():
    global p
    if (p == False):
        p = True
    else:
        p = False
        start()


def rerun():
    global xb, yb, ha, hb, r, speed, staspeed, aa, bb, p, wins
    if (wins == False): return
    t.reset()
    t.hideturtle()
    t.tracer(False)
    staspeed = 3
    speed = staspeed
    ha = -50
    hb = -50
    xb = 0
    yb = 0
    r = 0
    aa = 0
    bb = 0
    p = False
    wins = False
    start()


def move():
    global xb, yb, ha, hb, r, speed, staspeed, aa, bb, p, wins
    ##判断暂停
    if (p): return

    ##上下墙壁反弹
    if (yb >= 290): r = -abs(r)
    if (yb <= -290): r = abs(r - 360)
    ##球拍反弹
    if (xb >= 355 and (yb - ha) <= 115 and (yb - ha) >= -15):
        r = -(yb - ha + 15) / 130 * 135 + 247.5
        speed = abs((yb - ha + 15) / 130 - 0.5) * 2 + staspeed
    if (xb <= -355 and (yb - hb) <= 115 and (yb - hb) >= -15):
        r = (yb - hb + 15) / 130 * 135 - 67.5
        speed = abs((yb - hb + 15) / 130 - 0.5) * 2 + staspeed

    ##输球
    if (xb >= 400):
        xb = 0
        yb = 0
        r = 0
        aa += 1
        speed = staspeed
    if (xb <= -400):
        xb = 0
        yb = 0
        r = 180
        bb += 1
        speed = staspeed

    if (aa == 10):
        t.reset()
        t.write("PLAYER A WINS", align="center", font=("Arial", 40, "normal"))
        t.goto(0, -100)
        t.write("Press 'R' to restart", align="center", font=("Arial", 20, "normal"))
        wins = True
    if (bb == 10):
        t.reset()
        t.write("PLAYER B WINS", align="center", font=("Arial", 40, "normal"))
        t.goto(0, -100)
        t.write("Press 'R' to restart", align="center", font=("Arial", 20, "normal"))
        wins = True

    if (wins): return

    t.clear()
    ##
    bg()
    playerA(ha)
    playerB(hb)
    ##
    ##
    ball(xb, yb)
    xb += dir.x(radians(r))
    yb += dir.y(radians(r))
    ##
    score(aa, bb)

    t.update()


def start():
    while (1):
        move()
        if (p or wins): return


##初始化游戏参数
staspeed = 2
speed = staspeed
ha = -50
hb = -50
xb = 0
yb = 0
r = 0
aa = 0
bb = 0
p = False
wins = False
################
t.hideturtle()
t.tracer(False)
################
t.listen()
t.onkeypress(lambda: moveA(4), "Up")
t.onkeypress(lambda: moveA(-4), "Down")
t.onkeypress(lambda: moveB(4), "w")
t.onkeypress(lambda: moveB(-4), "s")
t.onkeypress(lambda: pause(), "p")
t.onkeypress(lambda: rerun(), "r")

start()

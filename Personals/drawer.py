import random
import turtle
from Personals.colorconverter import hex_to_rgb1

color_list = ["0f211b","083829","004f36","b5ca8d","daedbd","eee1b3"]

# convert to rgb1
color_list = hex_to_rgb1(color_list)

def form_hex(side):
    my_pen.color(color_list[random.randrange(0, len(color_list))])
    for i in range(6):
        my_pen.fd(side)
        my_pen.left(360 / 6)


def form_row(number, side):
    for i in range(number):
        my_pen.up()
        my_pen.fd(side)
        my_pen.left(360 / 6)
        my_pen.fd(side)
        my_pen.left(-(360 / 6))
        my_pen.fd(side)
        my_pen.left(-(360 / 6))
        my_pen.fd(side)
        my_pen.left((360 / 6))
        my_pen.down()
        form_hex(side)


tut = turtle.Screen()
tut.bgcolor("black")
tut.title("look at em go")
startx = -(turtle.screensize()[0]/2)
starty = turtle.screensize()[1]/2

my_pen = turtle.Turtle()
my_pen.color("white")
my_pen.speed(50)
my_pen.up()
my_pen.setx(startx)
my_pen.sety(starty)
my_pen.down()

tut = turtle.Screen()

# for different shapes
side = 10
num = 10
row_num = 10
i = 1
for i in range(row_num):
    form_row(num, side)
    my_pen.up()
    i += 1
    my_pen.setx(startx + ((i % 2) * (side + 5)))
    my_pen.sety(starty + i * 8.66 + 1)

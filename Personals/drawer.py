# import the turtle modules
import random
import turtle

# color list
# inital hex input
color_list = ["f2c166","174a75","133d61","6592e6","5d81a1","fcdb9d"]

# convert to rgb255
for i in color_list:
    color_list[color_list.index(i)] = tuple([int(i[0:2], 16), int(i[2:4], 16), int(i[4:6], 16)])

# convert to rgb1.0
for i in color_list:
    temp = [i[x] for x in range(0, 3)]
    for x in temp:
        temp[temp.index(x)] = round(x/255, 4)
    temp = tuple(temp)
    color_list[color_list.index(i)] = temp

# define the function
# for triangle
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


# Forming the window screen
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

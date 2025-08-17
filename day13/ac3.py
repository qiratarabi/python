import turtle
my_Wn = turtle.Screen()
my_Wn.bgcolor("light blue")
qirat = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        qirat.fd(size+1)
        qirat.left(90)
        size = size - 5
    size = size + 1


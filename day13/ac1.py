import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)
qirat = turtle.Turtle()
side = int(input("Enter the number of sides"))
angle = 360/side
for i in range(0, side):
    qirat.forward(100)
    qirat.left(angle)
turtle.done()


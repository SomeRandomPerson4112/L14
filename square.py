import turtle
turtle.shape("circle")
turtle.Screen().bgcolor("red")
num_sides=4
side_length=200
angle=90
turtle.Turtle()
for i in range(num_sides):
    turtle.fillcolor("green")
    turtle.forward(side_length)
    turtle.right(angle)
turtle.done()
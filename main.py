import random
import turtle
s = turtle.Screen()
t = turtle.Turtle()

max = 50

t.speed(0) 

for yAxisShape in range(3):
  for xAxisShape in range(3):
    for hPos in range(-max, max+1, 5):
      t.up()
      t.goto(200*xAxisShape, -200*yAxisShape)
      t.down()
      t.right(20)
      vert = random.randrange(1, 2*max+1)
      random_color=(random.random()*255, 0, 0)
      t.pencolor(random_color)
      t.forward(vert)

s.exitonclick()
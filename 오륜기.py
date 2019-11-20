import turtle

def screenCircle(x, y) :
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.circle(50)

turtle.shape('turtle')

screenCircle(-90, 0)
screenCircle(0, 0);
screenCircle(90, 0)

screenCircle(-45, -70)
screenCircle(44, -70)

turtle.done()

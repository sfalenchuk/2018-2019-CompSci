import turtle

turtle.color('red')

while True:
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    if abs(pos()) < 1:
        break
done()
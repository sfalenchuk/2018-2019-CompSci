#Sasha
#Basic dartboard, cant figure out straight line from center to dart
import random


def stroll(w):
	a = random.uniform(-1,1)
	b = random.uniform(-1,1)
	x, y = 0, 0
	for i in range(w):
		(dx,dy) = random.choice([(a,b),(a,b),(a,b),(a, b)])
		x += dx
		y += dy
	return (x,y)

for i in range(25):
	dart = stroll(1)
	print(dart, "Distance from home = ", abs(dart[0])  + abs(dart[1]))



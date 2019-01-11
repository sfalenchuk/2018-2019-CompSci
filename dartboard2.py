#Sasha
#Tried some more, but after the better part of 2 hours (roughly an hour forty five) I decided to stop here.
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

numthrows = 100

for length in range(0, 1):
	boarddistance = 0
	for i in range(numthrows):
		(x, y) = stroll(length)
		distance = abs(x) + abs(y)
		if distance <= 1:
			boarddistance += 1
	returnpercentage = float(boarddistance) / numthrows
	print("dart distance = ", length, " / %  of hit = ", 100*returnpercentage)
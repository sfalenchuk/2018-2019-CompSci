#Sasha
#Sources: Used stack overflow and some helpful videos
#I found that the max number of spaces you can travel to have at least a 50% chance of getting back home is 22.0
#Monte Carlo simulations can be used to determine probability and risk
import random

def stroll(w):
	x, y = 0, 0
	for i in range(w):
		(dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1, 0)])
		x += dx
		y += dy
	return (x,y)

numwalks = 10000

for length in range(1,31):
	returnhome = 0
	for i in range(numwalks):
		(x, y) = stroll(length)
		distance = abs(x) + abs(y)
		if distance <= 4:
			returnhome += 1
	returnpercentage = float(returnhome) / numwalks
	print("walk length = ", length, " / %  of no transport = ", 100*returnpercentage)


	
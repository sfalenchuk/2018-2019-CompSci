import random

def stroll(w):
	x, y = 0, 0
	for i in range(w):
		(dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1, 0)])
		x += dx
		y += dy
	return (x,y)

for i in range(25):
	walk = stroll(10)
	print(walk, "Distance from home = ", abs(walk[0])  + abs(walk[1]))
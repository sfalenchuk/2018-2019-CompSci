import random

i = []

for x in range (10):
	r = random.randrange(0,100,1)
	if r % 3 is 0 or r % 2 is 0 and r % 6 is not 0:
		i.append(r)








#for i in range(0, 100, 3):
print (i)
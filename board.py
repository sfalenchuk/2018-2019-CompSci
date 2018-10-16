import random
import sys

def print_mylist():
	for j in mylist[1:-1]:
		print(*j[1:-1])

row = int(sys.argv[1])+2
columns = int(sys.argv[2])+2
bombs = int(sys.argv[3])


mylist = [[0]*columns for x in range (row)]

#print board

for i in range (bombs):
	down = random.randrange(1,row-1,1)
	over = random.randrange(1,columns-1,1)
	while mylist[down][over] is "*":
		down = random.randrange(1,row-1,1)
		over = random.randrange(1,columns-1,1)
	mylist[down][over] = "*"

	if mylist[down][over-1] is not "*":
		mylist[down][over-1] += 1

	if mylist[down][over+1] is not "*":
		mylist[down][over+1] += 1

	if mylist[down-1][over+1] is not "*":
		mylist[down-1][over+1] += 1

	if mylist[down-1][over] is not "*":
		mylist[down-1][over] += 1

	if mylist[down-1][over-1] is not "*":
		mylist[down-1][over-1] += 1

	if mylist[down+1][over-1] is not "*":
		mylist[down+1][over-1] += 1

	if mylist[down+1][over] is not "*":
		mylist[down+1][over] += 1

	if mylist[down+1][over+1] is not "*":
		mylist[down+1][over+1] += 1

print_mylist()
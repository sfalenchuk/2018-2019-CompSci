import random
import sys

row = int(sys.argv[1])+2
columns = int(sys.argv[2])+2
bombs = int(sys.argv[3])

mylist = [[0]*columns for x in range (row)]


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

choiceoption = input("do you want to flag or choose?")

if choiceoption == flag:
	choiceflag = input("what space do you want to flag")

if choiceoption == choose:
	choicespace = input("what space do you choose?")

for j in mylist[1:-1]:
	print(*j[1:-1])

for down  in range (0, len(mylist)):
	for over in range (0, (len(mylist[0]))
		
if mylist[down][over] == "*"
	print("Game Over!")








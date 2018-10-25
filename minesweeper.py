import random
import sys

def print_mylist():
	for j in mylist[1:-1]:
		print(*j[1:-1])


def print_game():
	for v in game[1:-1]:
		print(*v[1:-1])

def reveal_zero(over,down):
	zerolist = []
	zerolist.append([over, down])
	while len(zerolist) > 0:
		over, down = zerolist.pop(0)
		for o in range (-1,2):
			for d in range (-1,2):
				if mylist[over+o][down+d] == 0 and game[over+o][down+d] == 'x':
					zerolist.append([over+o,down+d])
				game[over+o][down+d] = mylist[over+o][down+d]

#zeros in gutter
#if you uncover a zero, and in uncovering you uncover another a zero next to it, no infinite loops.




row = int(sys.argv[1])+2
columns = int(sys.argv[2])+2
bombs = int(sys.argv[3])

game = [["x"]*columns for x in range (row)]

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

mylist[0] = [1]*columns
mylist[-1] = [1]*columns

for y in range (row):
	mylist[y][0] = 1
	mylist[y][-1] = 1

#print_mylist()

print_game()


while True:

	choiceoption = input("do you want to flag or choose?")

	if choiceoption == "flag":
		choiceflag = input("what space do you want to flag")
		coords = choiceflag.split(",")
		over = int(coords[0] )
		down = int(coords[1] )
		game[down][over] = "P"
		# print_game()

	elif choiceoption == "choose":
		choicespace = input("what space do you choose?")
		coords = choicespace.split(",")
		over = int(coords[0] )
		down = int(coords[1] )
		game[down][over] = mylist[down][over]
		# print_game()

		if mylist[down][over]== 0:
			
			reveal_zero(over,down)

			

		elif mylist[down][over]  == "*":
			print_mylist()
			print("nice try, you lose.")
			quit()

		elif mylist[down][over] >= 1 or mylist[down][over] <= 9:
			game[over][down] == mylist[over][down]


	
	print_game()





# for down  in range (0, len(mylist)):
# 	for over in range (0, (len(mylist[0]))
		
# if mylist[down][over] == "*"
# 	print("Game Over!")






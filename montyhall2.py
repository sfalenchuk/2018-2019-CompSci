#Sasha
#1/9/19
#Monty Hall Simultion 1000 times no switch
#better to switch, because odds increase
import random

tries = 0

while tries < 1000:
	tries += 1
	gooddoor = random.randint(1,3)
	print(gooddoor)
	choice = random.randint(1,3)
	#representing possible wrong doors
	wrongone = gooddoor + 1
	wrongtwo = gooddoor - 1
	if wrongone >= 1 and wrongone <= 3 and wrongone != gooddoor and wrongone != int(choice):
	#making sure wrongone fits within our three doors, since it could theoretically be 4 if gooddoor is 3
		choicesecond = choice
		if int(choicesecond) != gooddoor:
			print("sorry you lose!")
		elif int(choicesecond) == gooddoor:
			print("nice!")
	elif wrongtwo != gooddoor and wrongtwo != int(choice):
		choicesecond = 1
		if int(choicesecond) != gooddoor:
			print("sorry!")
		elif int(choicesecond) == gooddoor:
			print("nice job!")
	else:
		choicesecond = 1
		if int(choicesecond) != gooddoor:
			print("sorry!")
		elif int(choicesecond) == gooddoor:
			print("nice job!")


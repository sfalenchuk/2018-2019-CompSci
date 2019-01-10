#Sasha
#1/9/19
#Monty Hall Simultion
#better to switch, because odds increase
import random

tries = 0

while tries < 100:
	tries += 1
    gooddoor = random.randint(1,3)
	print(gooddoor)
	choice = input("You have three doors, behind two are pennies, and behind the other one is a set of brand new car keys! Which one do you choose")
	#representing possible wrong doors
	wrongone = gooddoor + 1
	wrongtwo = gooddoor - 1
	if wrongone >= 1 and wrongone <= 3 and wrongone != gooddoor and wrongone != int(choice):
	#making sure wrongone fits within our three doors, since it could theoretically be 4 if gooddoor is 3
		choicesecond = input ("go ahead and give me a final answer you can switch just keep in mind there is a penny behind door " + str(wrongone) + ", good luck and pick a door!")
		if int(choicesecond) != gooddoor:
			print("sorry you lose!")
		elif int(choicesecond) == gooddoor:
			print("nice!")
	elif wrongtwo != gooddoor and wrongtwo != int(choice):
		choicesecond = input ("go ahead and give me a final answer you can switch just keep in mind there is a penny behind door " + str(wrongtwo) + ", good luck and pick a door!")
		if int(choicesecond) != gooddoor:
			print("sorry!")
		elif int(choicesecond) == gooddoor:
			print("nice job!")
	else:
		choicesecond = input ("go ahead and give me a final answer you can switch just keep in mind there is a penny behind door " + str(wrongtwo) + ", good luck and pick a door!")
		if int(choicesecond) != gooddoor:
			print("sorry!")
		elif int(choicesecond) == gooddoor:
		print("nice job!")






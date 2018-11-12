def binary():

	number = int(input("Enter a binary number"))

	numberseparated = list(str(number))

	decimal = 0

	counter = 0

	for i in reversed(numberseparated):
		decimal += 2**counter * int(i)
		counter+=1

	print("The decimal number is, ", decimal)

binary()
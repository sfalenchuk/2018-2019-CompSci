def moves(n, left):
#n determines the different disc sizes, and left is a boolean which is either true or false
	if n==0:
		return
#base case, says that there is no tower, so nothing can happen
	moves(n-1,not left)
	if left:
		print(str(n) + 'left')
	else:
		print(str(n) + 'right')
	 moves(n-1, not left)
moves(5,True)
#here i am just assigning values to the first 2 variables
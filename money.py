class Money:

	def __init__(self, amount,):
		self.amount = amount

	def __str__(self):
		amount = self.amount
		if self.amount == 50:
			amount = "Red"
		if self.amount == 100:
			amount = "Green"
		if self.amount == 250:
			amount = "Blue"
		if self.amount == 500:
			amount = "Black"
		if self.amount == 1000:
			amount = "White"
		return str(amount)+" chip"
	__repr__ = __str__
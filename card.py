class Card:

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		rank = self.rank
		if self.rank == 11:
			rank = "Jack"
		elif self.rank == 12:
			rank = "Queen"
		elif self.rank == 13:
			rank = "King"
		elif self.rank == 1:
			rank = "Ace"
		return str(rank)+" of "+self.suit

	__repr__ = __str__



		





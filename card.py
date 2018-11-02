class Card:
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		status = ""
		rank = self.rank
			if self.rank = 1
				rank = "Ace"
			elif self.rank = 11
				rank = "Jack"
			elif self.rank = 12
				rank = "Queen"
			elif self.rank = 13
				rank = "King"



		return self.rank +"of"+ self.suit

c1 = Card(1,"Hearts")
c2 = Card(6,"Hearts")
c3 = Card(13,"Hearts")

print(c1,c2,c3)

# class Deck:
# 	def __init__(self):
# 		self.cards = []
# 		for i in range(1, 14)
# 			self.cards.append(Card(i,"Spades")
# 			self.cards.append(Card(i,"Hearts")
# 			self.cards.append(Card(i,"Clubs")
# 			self.cards.append(Card(i,"Diamonds")





from card import Card
from random import shuffle

class Deck:

	def __init__(self, full_deck=-1):
		if full_deck == -1:
			suits = ["Spades","Hearts","Clubs","Diamonds"]
			self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in suits]
			self.shuffle()
		else:
			self.cards = []

	def shuffle(self):
		shuffle(self.cards)

	def deal(self, position=-1):
		if position==-1:
			return self.cards.pop(0)
		else:
			return self.cards.pop(position)

	def add_card(self, card):
		self.cards.append(card)

	def num_cards(self):
		return len(self.cards)

	def contains(self, card):
		for i in self.cards:
			if card.rank == i.rank and card.suit == i.suit:
				return True
		return False

	def __str__(self):
		result = ''
		for i in self.cards:
			result += str(i)+"\n"
		return result

	__repr__ = __str__


deck = Deck()
print(deck)



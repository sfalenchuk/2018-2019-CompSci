import random
from card import Card
from deck import Deck
from random import shuffle

# class Person:
#     def __init__(self):
#         self.name = name
#         self.status = status

# class Hand:
#     def __init__(self):
#         self.hand = []

#     def add_card(self, card):
#         self.hand.append(card[0])
#         return self.hand
def checkstatus(pchoice, dchoice):
   
    dhand = 0;

    for card in dealer_hand.cards:
        dhand += card.rank

    hand = 0;

    for card in player_hand.cards:
        hand += card.rank


    if dhand == 21 or (dhand < 21 and hand > 21):
        print("dealer wins")
        

    if hand == 21 or (hand < 21 and dhand > 21):
        print("player wins")

    if pchoice == "stand" or dchoice == "stand":
        
        if hand > dhand:
            print("player wins, dealer stands")

        if dhand > hand:
            print("dealer wins, player stands")

        if hand == dhand or (hand > 21 and dhand > 21):
            print ("bust, play again")








deck = Deck()
dealer_hand = Deck(0)
player_hand = Deck(0)

# dealer = Person()
# player = Person()

print("Hello, and welcome to Blackjack. Blackjack is an advanced gambling game in which it is your job to reach the number 21")

print("You will start out with one card, and after that you will have a choice to hit or pass. If you hit, you will get another card, in an attempt to get closer to 21. But be careful, get over 21 and you will lose!")

print("The game will continue until the players finish their turns, and then everyone will reveal their cards")

choice = input("All players start with ten thousand dollars, ready to begin?")


if choice == "yes":

    player_hand.add_card(deck.deal())

    dealer_hand.add_card(deck.deal())

    hand = 0;

    for card in player_hand.cards:
        hand += card.rank

    while hand < 21:
        print(player_hand)

        playerchoice = input("Do you hit or stand?")
           

        if playerchoice == "hit":
            player_hand.add_card(deck.deal())

            dhand = 0;

            for card in dealer_hand.cards:
                dhand += card.rank
            
            if dhand < 16:
                dealerchoice = "hit"
                dealer_hand.add_card(deck.deal())

                checkstatus(playerchoice, dealerchoice)
            else:
                dealerchoice = "stand"
                print("dealer stands")

                result = checkstatus(playerchoice, dealerchoice)

elif choice == "no":
    print("Alright, read the rules again")





    









            
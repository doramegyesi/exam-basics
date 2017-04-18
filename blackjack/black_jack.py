# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors
# (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades

import random

class Card():
    def __init__(self, color = "", value = ""):
        self.color = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.card = self.value + self.color

    def show_some_cards(self):
        self.list_of_cards =[]
        for c in self.color and v in self.value:
            list_of_cards = [v + c]
        return list_of_cards

class Deck(Card):
    def __init__(self, color, value="", number =""):
        self.number = number
        self.list_of_cards = []



deck = Card(12)

print(deck.show_some_cards())

print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
#top_card = deck.draw()
#print(top_card)
#print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades

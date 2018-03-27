'''
Kodiak Conrad
kconrad1@uw.edu
Passur Game State
'''

import sys
import ast
import priorityQB as pq
import heapdictB as hd
import random



class Card:
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

class Deck:
	suit_list = [spades, clubs, hearts, diamonds]
	deck = []
	def __init__():
		for suit in suit_list:
			for n in range(1, 14):
				card = Card(n, suit)
				deck.add(card)
		self.deck = random.permutation(deck)
		self.cards_left = 52

def playgame();
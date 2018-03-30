'''
Kodiak Conrad
kconrad1@uw.edu
Passur Game Manager
'''

import sys
import ast
import priorityQB as pq
import heapdictB as hd
import random

from passur_state import passur_state as passur

import sys, importlib.util


'''passur_game_manager passur player1 player2'''

if sys.argv==[''] or len(sys.argv)<2:
    print("For AI game, type python3 passur_game_master.py passur_client passur_AI")
    print("For 2-player game, replace passur_AI with passur_client")
    exit(0)

player1 =importlib.import_module(sys.argv[1])
player2 =importlib.import_module(sys.argv[2])

deck = Deck()
INITIAL_STATE = passur_state(deck, [], [], 0, 0, deck.cards_left)

def playgame():
	current_state = INITIAL_STATE
	print("Welcome to Passur")
	print("Would you like to view instructions?")
	board = []
	p1hand = []
	p2hand = []
	answer = input("Y or N? >> ")
      if answer=="Y" or answer=="y": showinstrutions()
      for i in range 4:
      	card = INITIAL_STATE.deck.remove()
      	current_state.board.append(card)
    while current_state.cards_left > 0:
    	for i in range 4:
    		c1 = current_state.deck.remove()
    		p1hand.append(c1)
    		c2 = current_state.deck.remove()
    		p2hand.append(c2)
    	print(current_state)
    	while len(p2hand) > 0:
    		state = current_state.copy()
    		[board, points_gained, card_played] = player1.make_move(state)
  			state.board = board
  			state.gone = state.gone.append(card_played)
  			state.p1points += points_gained
  			if (not board and card_played.number != 11 and state.deck.size > 0):
  				state.p1points += 5
    		[board, points_gained, card_played] = player2.make_move(tate)
    		state.board = board
    		state.gone = state.gone.append(card_played)
    		state.p2points += points_gained
    		if (not board and card_played.number != 11 and state.deck.size > 0):
  				state.p2points += 5
    		#Next step is to write make move function for client


class Card:
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

	def __str__(self):
		if self.number == 1: n = "Ace"
		elif self.number < 10:
			n = str(self.number)
		else:
			if self.number = 11: n = "Jack"
			if self.number = 12: n = "Queen"
			if self.number = 13: n = "King"
		return n + " of " + self.suit

	def __eq__(self, other):
		return self.suit == other.suit and self.number == other.number:

	def __hash__(self):
    	return (str(self)).__hash__() 

class Deck:
	suit_list = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
	deck = []
	def __init__(self):
		for suit in suit_list:
			for n in range(1, 14):
				card = Card(n, suit)
				deck.add(card)
		self.deck = random.shuffle(deck)
		self.cards_left = 52
	def remove(self):
		cards_left -= 1
		card = self.deck.remove()
		return card

	def __eq__(self, other):
		if self.cards_left != other.cards_left:
			return false
		if self.deck != other.deck:
			return false
		return true

def showinstructions():
	print("Oops, no instructions available yet")

if __name__ == '__main__':
    playgame()
    print("The session is finished.")











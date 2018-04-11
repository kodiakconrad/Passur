'''
Kodiak Conrad
kconrad1@uw.edu
Passur Client User
'''

import sys
import ast
import priorityQB as pq
import heapdictB as hd
import random
import passur_state as passur

class My_State():
#My state keeps track of what cards I have in my hand
'''After we get gameplay working, we can include state values for cards owned by both players.
   The game manager keeps track of points, and what to do with a card once it is played,
   it is our job to just make a decision and nothing else''' 
	def __init__(board, hand):
		self.board = board
		self.hand = hand
		self.all_moves = [(card, place) for card in hand for place in board]

	def __str__(self):
		for x in hand:
			print(x)

	def __eq__(self, other):
		if len(self.hand) != len(other.hand): return false
		for card in self.hand:
			if card not in other.hand: return false
		return true

	def __hash__(self):
    	return (str(self)).__hash__() 

	def copy(self):

	def can_move(self, card, position):

	def move(self, card, position):


def make_move(board, hand):
	state = My_State(board, hand)

	OPERATORS = [passur.Operator(
	"Place "+str(card)+" on position "+str(pos),
	lambda s, c1=card, p1=pos: s.can_move(card, pos),
	lambda s, c1=card, p1=pos: s.move(card, pos) )
	for (card, pos) in state.all_moves

	# mext step is to write can move and move functions in the state file
	# maybe only involve operators at manager level? not have as part of client? 
	# we can deal with that problem later, but first we should have the methods written. 






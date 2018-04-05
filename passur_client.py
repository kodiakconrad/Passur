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
from passur_state import passur_state as passur

class My_State():
#My state keeps track of what cards I have in my hand
'''After we get gameplay working, we can include state values for cards owned by both players.
   The game manager keeps track of points, and what to do with a card once it is played,
   it is our job to just make a decision and nothing else''' 
	def __init__(hand):
		self.hand = hand

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

	def all_moves(self, current_state):
		moves = []
		for card in self.hand:
			for place in current_state.board:	
				moves.add(card,place)
		return moves

	def make_move(current_state):
		OPERATORS = [passur.Operator(
		"Place "+str(card)+" on position "+str(pos),
		lambda s, c1=card, p1=pos: s.can_move(card, pos),
		lambda s, c1=card, p1=pos: s.move(card, pos) )
		for (card, pos) in all_moves(current_state)]

		# mext step is to writ can move and move functions in the state file
		# the code above will not run the file as expected because it can not access those two methods
		# we can deal with that problem later, but first we should have the methods written.

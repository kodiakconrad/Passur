'''
Kodiak Conrad
kconrad1@uw.edu
Passur Game State
'''



class Passur_State:
	def __init__(self, deck, board, gone, cardsleft, p1points, p2points):
		self.deck = deck 
		self.board = board
		self.gone = gone
		self.p1points = p1points
		self.p2points = p2points
		self.cardsleft = cardsleft

	def __str__(self):
		for x in board:
			print(x)
		print("There are " + str(self.cardsleft) + " cards left")

	def __eq__(self, other):

	def __hash__(self):

	def copy(self):

	def can_move(self, card, position):

	def move(self, card, position):

	def goal_test(s):

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

GOAL_TEST = lambda s: goal_test(s)
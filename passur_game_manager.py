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

import sys, importlib.util

# Get the PROBLEM name from the command-line arguments

'''passur_game_manager passur player1 player2'''

if sys.argv==[''] or len(sys.argv)<2:
    print("For AI game, type python3 passur_game_master.py passur_client passur_AI")
    print("For 2-player game, replace passur_AI with passur_client")
    exit(0)
  
game = importlib.import_module("passur")

player1 =importlib.import_module(sys.argv[1])
player2 =importlib.import_module(sys.argv[1])

OPERATORS=PROBLEM.OPERATORS
STATE_STACK = []
TITLE="Passur Game Manager"




def playgame():
	print("Welcome to Passur")
	print("Would you like to view instructions?")
	answer = input("Y or N? >> ")
      if answer=="Y" or answer=="y": showinstrutions()



def showinstructions():
	print("Oops, no instructions available yet")

if __name__ == '__main__':
    playgame()
    print("The session is finished.")











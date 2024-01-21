import math
import random 

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__ (self, letter):
        super().__init__(letter)

    def get_move(self, game):
        sqaure = random.choice(game.available_moves())
        return sqaure

class HumanPlayer(Player):
    def __init__ (self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            sqaure = input(self.letter + '\s turn. Input Move (0-8):')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid 
            # if that spot is not avalable on the board, we also say it's invalid if
            try:
                val = int(sqaure)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid sqaure. Try Again.')

        return val 
                





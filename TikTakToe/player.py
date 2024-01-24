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

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            sqaure = random.choice(game.available_moves())   # randomly choose one 
        else:
            # get the sqaure based off the minimax algorithm
            sqaure = self.minimax(game, self.letter)
        return sqaure
    
    def minimax(self, state, player):
        max_player = self.letter #Literally Yourself!
        other_player = 'O' if player == 'X' else 'X' # the other plater (whenever the letter is NOT X)


        # first, we want to check if the previous move is a winner or
        # this is our base case 

        if state.current_winner == other_player:
            # we should return posistion AND score because we need to keep track of the score 
            # for minimax to work
            return {'position': None, 
                    'score': 1 * (state.num_empty_sqaures() + 1) if other_player == max_player else -1 * 
                        (state.num_empty_sqaures() + 1) 
                    }
        elif not state.num_empty_sqaures(): #no empty sqaures
            return {'posistion': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize 

        for  possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after make the move and
            sim_score = self.minimax(state, other_player) # now we alterante players 
            
            # step 3: undo the move 
            state.board[possible_move] = ' '
            state.current_winner = None 
            sim_score['position'] = possible_move # othersie this will get messed up from the recursion 
            
            # step 4: update the dictionaries if nessesary 
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best
        
        return best









                





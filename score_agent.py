# Put your name and student ID here before submitting!
# Merijn Schepers (6504477)

from random_agent import RandomAgent

import numpy as np
import time
import copy

class Agent:
    def __init__(self, iterations, id):
        self.iterations = iterations
        self.id = id


    def simulate(self, move, game):
        g = copy.deepcopy(game)
        g.board.place(move, self.id)
        if(g.victory(move, self.id)):
            return 1
        if(g.board.full()):
            return 0.5
        g.print_board = False
        # replace players by randomagents, opponent goes first
        g.players = [RandomAgent(1 if (self.id == 2) else 2), RandomAgent(self.id), ]
        winner = g.play()
        
        # reward 0.5 for draw, 1 for win and 0 for loss
        if winner is None:
            return 0.5
        elif winner.id is self.id:
            return 1
        return 0


    def make_move(self, game):
        moves = game.board.free_positions()
        scores = [0] * len(moves)
        enemy_id = 2 if (self.id == 1) else 1

        for i in range(len(moves)):
            #c1 = copy.deepcopy(game)
            
            game.board.place(moves[i], self.id)

            # if we win, score + 100
            if(game.victory(moves[i], self.id)):
                #print('victory found')
                scores[i] += 100
            else:
                # simulate all next moves
                next_moves = game.board.free_positions()
                for next_move in next_moves:
                    # first check ourselves
                    game.board.place(next_move, self.id)
                    # if the we win, score + 1
                    if(game.victory(next_move, self.id)):
                        scores[i] += 1
                    # then check opponent
                    game.board.place(next_move, enemy_id)
                    # if the we win, score - 1
                    if(game.victory(next_move, enemy_id)):
                        scores[i] -= 1
                    # undo the move
                    game.board.place(next_move, 0)
            # undo the move
            game.board.place(moves[i], 0)
        
        max_score = max(scores)
        best_moves = [m for m in range(len(scores)) if scores[m] == max_score]
        # print(moves)
        # print(scores)
        # print(best_moves)
        return moves[np.random.choice(best_moves)]


    def __str__(self):
        return f'Player {self.id} (your agent)'
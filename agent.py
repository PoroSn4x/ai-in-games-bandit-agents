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
        if(g.board.victory(move, self.id)):
            return 1
        g.print_board = False
        # replace players by randomagents, opponent goes first
        g.players = [RandomAgent(1 if (self.id == 2) else 2), RandomAgent(self.id)]
        winner = g.play()
        # reward 0.5 for draw, 1 for win and 0 for loss
        if winner is None:
            return 0.5
        elif winner is g.players[1]:
            return 1
        return 0



    def make_move(self, game):
        i = 0

        # available moves
        moves = game.board.free_positions()
        # rewards per arm
        rewards = []
        # tries per arm
        tries = []    

        rewards = np.repeat([0], len(moves))
        tries = np.repeat([0], len(moves))

        # run until time is up
        while i < self.iterations:
            # randomly explore a move
            move = np.random.randint(0, len(moves))
            result = self.simulate(moves[move], game)
            rewards[move] += result
            tries[move] += 1
            i += 1

        # select move with highest expected value
        for i in range(len(rewards)):
            if(tries[i] > 0):
                rewards[i] /= tries[i]
        bestmove = np.argmax(rewards)
        return moves[bestmove]



    def __str__(self):
        return f'Player {self.id} (your agent)'
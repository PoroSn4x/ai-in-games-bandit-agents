# Put your name and student ID here before submitting!
# Merijn Schepers (6504477)

from contextlib import nullcontext
from random_agent import RandomAgent
from operator import attrgetter

from game import Game
import numpy as np
import math
import time
import copy


C = 1.5

class Node:
    # old board
    def __init__(self, parent, move, id, board):
        self.parent = parent
        self.move = move
        self.id = id
        self.board = board
        self.children = []
        self.t = 0
        self.n = 0

    # calculates uct
    def UCT(self):
        if(self.n == 0):
            return 99999999999999

        return self.t + C * math.sqrt(math.log(self.parent.n) / self.n)


class Agent:
    def __init__(self, iterations, id):
        self.iterations = iterations
        self.id = id

    def simulate(self, node, game):
        #print('simulate')
        players = [RandomAgent(1 if node.id == 2 else 2), RandomAgent(node.id)]
        #g = copy.deepcopy(game))
        g = Game.from_board(copy.deepcopy(node.board), game.objectives, players, False)
        
        # first check if game is already over
        if(g.victory(node.move, node.id)):
            return 5 if node.id == self.id else -5
        if(g.board.full()):
            return 0

        winner = g.play()

        if winner is None:
            return 0
        elif winner.id is self.id:
            return 5
        return -5

    def select(self, node):
        #print('select')
        # calculate utc of children and return (random) best one
        ucts = []
        for child in node.children:
            ucts.append(child.UCT())
        
        best_children = [node.children[i] for i in range(len(ucts)) if ucts[i] == max(ucts)]
        #print(best_children)
        #time.sleep(2)
        return np.random.choice(best_children)

    def expand(self, node):
        #print('expand')
        moves = node.board.free_positions()
        turn = 1 if node.id == 2 else 2
        for move in moves:
            board_copy = copy.deepcopy(node.board)
            board_copy.place(move, turn)
            child = Node(node, move, turn, board_copy)
            node.children.append(child)

    def backpropagate(self, node, value):
        #print('backpropagate')
        n = node
        while n != None:
            n.t += value
            n.n += 1
            n = n.parent

    def make_move(self, game):
        opponent_id = 1 if self.id == 2 else 2
        root = Node(None, 0, opponent_id, game.board)
        
        # create initial children
        self.expand(root)
        for i in range(self.iterations):
            node = root
            # select child with highest uct until we have a leaf
            while node.children != []:
                node = self.select(node)
                #print(node)

            
            # the only situation where we expand a child, is on our second visit
            # the first visit we have to do a rollout
            # beyond the second visit means that this is a final board state, so we also do a rollout
            if node.n == 1:
                self.expand(node)
                node = self.select(node)

            value = self.simulate(node, game)
            self.backpropagate(node, value)

        # select child with highest t
        max_t = max(root.children, key=attrgetter('t')).t
        best_moves = [child for child in root.children if child.t == max_t]
        print(max_t)
        print(best_moves)
        return np.random.choice(best_moves).move


    def __str__(self):
        return f'Player {self.id} (your agent)'


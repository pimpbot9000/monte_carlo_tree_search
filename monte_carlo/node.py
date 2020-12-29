from typing import List
from monte_carlo.board import Board


class Node:
    def __init__(self, board: Board, parent=None, depth=0):
        self.depth = depth
        self.board: Board = board
        self.wins = 0
        self.n = 0
        self.parent: Node = parent
        self.children: List[Node] = []

    def has_children(self):
        return len(self.children) != 0

    def expand(self):
        moves = self.board.possible_moves()
        new_boards = [self.board.play_turn(move) for move in moves]
        self.children = [Node(new_board, parent=self, depth=self.depth+1) for new_board in new_boards]

    def is_terminal(self):
        return self.board.terminal

    def get_winner(self):
        if not self.is_terminal():
            raise Exception("Node is not terminal node. There is no winner")
        return self.board.winner

    def get_turn(self):
        return self.board.turn

    def get_previous_move(self):
        return self.board.previous_move

    @staticmethod
    def simulate(node):
        return Board.simulate(node.board)

    def __str__(self):
        return "visits: {visits}, wins: {wins}, depth: {depth}".format(visits=self.n,
                                                                       wins=self.wins,
                                                                       depth=self.depth)



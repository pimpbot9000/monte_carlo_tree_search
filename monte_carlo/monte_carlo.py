from monte_carlo.board import Board
from monte_carlo.node import Node
import math
import random


class MonteCarlo:
    def __init__(self, root: Node, nof_sims=1000, c=math.sqrt(2), verbose=True):
        self.root = root
        self.N = 0
        self.C = c
        self.nof_sims = nof_sims
        self.verbose = verbose

    def search(self):
        if self.verbose:
            print("Monte Carlo Tree Search... Searching")
        for _ in range(0, self.nof_sims):
            self.N += 1
            node = self.select_and_expand()

            if node.is_terminal():
                winner = node.get_winner()
            else:
                winner = self.simulate(node)

            self.back_propagate(node, winner, turn=self.root.get_turn())

        return self.get_best_move()

    def get_best_move(self):
        moves = list(map(lambda child: child.get_previous_move(), self.root.children))
        visits = list(map(lambda child: child.n, self.root.children))
        max_visits = max(visits)
        index = visits.index(max_visits)
        best_child = self.root.children[index]
        best_move = moves[index]

        if self.verbose:
            print("Win probability:", ((best_child.wins / best_child.n) + 1)/2)
            print("Move:", best_move)

        return best_move

    def select_and_expand(self):
        def _select(node: Node):
            if node.has_children():
                child = self.select_child(node)
                return _select(child)
            elif node.is_terminal():
                return node
            else:
                node.expand()
                child = self.select_child(node)
                return child

        return _select(self.root)

    def select_child(self, node: Node):
        uct_values = [self.uct(n) for n in node.children]
        max_uct = max(uct_values)

        choices = []

        for i, uct_val in enumerate(uct_values):
            if uct_val >= max_uct:
                max_uct = uct_val
                choices.append(node.children[i])

        return random.choice(choices)

    def uct(self, node: Node):
        """
        Upper Confidence bound for Trees 1
        UCT1 score is used for selection heuristic to balance exploration/exploitation.
        Node with the highest UCT1 score is the selected for the next child in tree traversal.

        The greater the value of C (>= 0) the more emphasis there is for an exploration.
        """
        if node.n == 0:
            return math.inf
        else:
            return node.wins / node.n + self.C * math.sqrt(math.log(self.N / node.n))

    @staticmethod
    def simulate(node: Node):
        return Board.simulate(node.board)

    def back_propagate(self, node: Node, winner, turn):
        node.n += 1

        if winner == node.get_turn():
            node.wins -= 1
        elif winner == 0:
            node.wins += 0
        else:
            node.wins += 1
        if node.parent is None:
            return
        else:
            self.back_propagate(node.parent, winner, turn)

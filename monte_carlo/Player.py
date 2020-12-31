from abc import abstractmethod, ABC

from monte_carlo.board import Board
from monte_carlo.minimax import Minimax
from monte_carlo.monte_carlo import MonteCarlo
from monte_carlo.node import Node
import random

class Player(ABC):
    """
    Abstract base class for a player (human or ai)
    """

    @abstractmethod
    def get_move(self, board: Board) -> int:
        """
        Abstract method that returns a move
        :param board: Board
        :return: int
        """
        pass


class PlayerMCTS(Player):

    def __init__(self, nof_sims=1000, c=1.4):
        self.nof_sims = nof_sims
        self.c = c

    def get_move(self, board: Board) -> int:
        mc = MonteCarlo(root=Node(board), nof_sims=self.nof_sims, c=self.c)
        move = mc.search()
        return move


class PlayerHuman(Player):
    def get_move(self, board: Board) -> int:
        possible_moves = board.possible_moves()
        print("possible moves", possible_moves)

        move = None

        while move is None:
            _input = input("Human, your turn! > ")

            try:
                _input = int(_input)
            except ValueError:
                print("Invalid input, not a number")
                continue

            if self.is_valid_move(_input, board):
                move = _input
            else:
                print("Invalid move")

        return move

    @staticmethod
    def is_valid_move(move, board: Board) -> bool:
        return move in board.possible_moves()


class PlayerMinimax(Player):

    def __init__(self, search_depth=8):
        self.search_depth = search_depth

    def get_move(self, board: Board) -> int:
        minimax = Minimax(max_depth=self.search_depth)
        return minimax.search(board)


class PlayerHarri(Player):
    def __init__(self):
        pass

    def get_move(self, board: Board) -> int:
        print("Harri is thinking very hard!")
        possible_moves = board.possible_moves()
        move = random.choice(possible_moves)
        print("Move:", move)
        return move


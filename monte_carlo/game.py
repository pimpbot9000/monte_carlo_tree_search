from monte_carlo.board import Board
from monte_carlo.tree_search import MonteCarlo
from monte_carlo.node import Node


class Game:
    def __init__(self):
        self.turn = 1
        self.board = None

    def play_human_vs_ai(self, starting_player=1, nof_sims=1000):
        self.board = Board(turn=starting_player)

        while self.board.winner == -1:
            self.board.print_board_info()
            self.board.print_board()
            move = int(input())
            self.board = self.board.play_turn(move)
            if self.board.terminal:
                break

            self.board.print_board_info()
            self.board.print_board()

            self.play_ai_turn(nof_sims=nof_sims)

        print("game over. winner = " + str(self.board.winner))
        self.board.print_board()

    def play_ai_vs_ai(self, starting_player=1, nof_sims=1000):
        self.board = Board(turn=starting_player)

        while self.board.winner == -1:
            self.play_ai_turn(nof_sims=nof_sims)
            self.board.print_board()

        print("game over. winner = " + str(self.board.winner))

    def play_ai_turn(self, nof_sims):
        mc = MonteCarlo(root=Node(self.board), nof_sims=nof_sims, c=5)
        print("ai thinking")
        ai_move = mc.search()
        self.board = self.board.play_turn(ai_move)


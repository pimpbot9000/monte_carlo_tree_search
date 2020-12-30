from monte_carlo.board import Board
from monte_carlo.minimax import Minimax
from monte_carlo.tree_search import MonteCarlo
from monte_carlo.node import Node


class Game:
    def __init__(self):
        self.board = None
        self.nof_sims = 1000
        self.max_depth = 8

    def play_human_vs_ai(self, starting_player=1):
        self.board = Board(turn=starting_player)

        while self.board.winner == -1:
            self.board.print_board_info()
            self.board.print_board()
            move = int(input("Human, your move! > "))
            self.board = self.board.play_turn(move)
            if self.board.terminal:
                break

            self.board.print_board_info()
            self.board.print_board()

            self.play_ai_turn(ai_type=starting_player)

        print("game over. winner = " + str(self.board.winner))
        self.board.print_board()

    def play_ai_vs_ai(self, starting_player=1):
        self.board = Board(turn=starting_player)

        while self.board.winner == -1:
            self.play_ai_turn(ai_type=self.board.turn)
            self.board.print_board()

        print("game over. winner = " + str(self.board.winner))

    def play_ai_turn(self, ai_type):
        ai_move = -1
        if ai_type == 1:  # Monte Carlo
            print("Monte Carlo Tree Search AI thinking (player {player})".format(player=ai_type))
            ai = MonteCarlo(root=Node(self.board), nof_sims=self.nof_sims, c=5)
            ai_move = ai.search()
        elif ai_type == 2: # Minimax
            print("Minimax AI thinking (player {player})".format(player=ai_type))

            max_depth = self.max_depth
            if self.board.count_pieces() >= 20:  # Change max depth
                max_depth = 14
                print("search depth", max_depth)

            ai = Minimax(max_depth)
            ai_move = ai.search(board=self.board, player=self.board.turn)

        self.board = self.board.play_turn(ai_move)


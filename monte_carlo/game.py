from monte_carlo.Player import PlayerMCTS, Player
from monte_carlo.board import Board


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board(turn=1)
        self.player1 = player1
        self.player2 = player2

    def start(self):

        self.board.print_board()

        while not self.board.terminal:
            print("Turn:", self.board.turn)
            player = self.get_player()
            move = player.play_turn(self.board)
            self.board = self.board.play_turn(move)
            self.board.print_board()

        print("Game over. Winner", self.board.winner)

    def get_player(self):
        """
        Get the player
        """
        if self.board.turn == 1:
            return self.player1
        elif self.board.turn == 2:
            return self.player2




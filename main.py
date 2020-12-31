from monte_carlo.board import Board
from monte_carlo.game import Game
import sys


def main(argv):
    game = Game()

    if argv[0] == "ai":
        game.play_ai_vs_ai(starting_player=1)
    if argv[0] == "human":
        game.play_human_vs_ai()


if __name__ == '__main__':
    main(sys.argv[1:])


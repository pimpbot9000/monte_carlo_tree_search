from monte_carlo.Player import PlayerMCTS, PlayerHuman, Player, PlayerMinimax
from monte_carlo.board import Board
from monte_carlo.game import Game
import sys


def main(argv):
    p1 = None
    p2 = None

    try:
        p1 = argv[0]
        p2 = argv[1]
    except IndexError:
        print_help()
        sys.exit()

    player1 = get_player(p1)
    player2 = get_player(p2)

    if player1 is None:
        print_help()
        sys.exit()

    if player2 is None:
        print_help()
        sys.exit()

    game = Game(player1, player2)
    game.start()


def get_player(val: str):
    if val == "human":
        return PlayerHuman()
    elif val == "mcts":
        return PlayerMCTS()
    elif val == "minimax":
        return PlayerMinimax()
    else:
        return None

def print_help():
    print("To select players:")
    print("python main.py [human|mcts|minimax] [human|mcts|minimax]")

if __name__ == '__main__':
    main(sys.argv[1:])


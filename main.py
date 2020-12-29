from monte_carlo.game import Game
import sys

def main(argv):
    game = Game()
    nof_sims = int(argv[1])

    if argv[0] == "ai":
        game.play_ai_vs_ai(nof_sims=nof_sims)
    if argv[0] == "human":
        game.play_human_vs_ai(1, nof_sims=nof_sims)


if __name__ == '__main__':
    main(sys.argv[1:])


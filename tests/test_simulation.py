from monte_carlo.board import Board
from monte_carlo.node import Node
from monte_carlo.tree_search import MonteCarlo
import numpy as np


def test_correct_move_to_win():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 0, 0],
        [0, 1, 2, 2, 2, 0, 0],
        [0, 1, 1, 1, 2, 0, 0],
        [0, 1, 2, 1, 2, 1, 0]
    ]

    move = search_move(raw_board=board, turn=2)
    assert move == 2


def test_correct_move_to_block_win():
    """
    Test for not blindly taking greedy move to win overlooking blocking enemy
    """
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0],
        [0, 0, 2, 1, 0, 2, 0]
    ]

    move = search_move(raw_board=board, turn=2)
    assert move == 3


def test_correct_move_to_win2():
    board = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 2, 0, 2, 2, 0, 0],
        [0, 1, 0, 1, 1, 2, 0],
        [0, 1, 0, 2, 2, 1, 0],
        [2, 1, 1, 1, 2, 1, 0],
        [1, 2, 1, 1, 2, 1, 2]
    ]

    move = search_move(raw_board=board, turn=1)
    assert move == 2


def search_move(raw_board, turn):
    board = Board(board=np.array(raw_board), turn=turn)
    mc = MonteCarlo(root=Node(board), nof_sims=1000)
    move = mc.search()
    return move


from monte_carlo.board import Board
import numpy as np

def test_no_winner():
    b1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2],
        [0, 1, 2, 1, 2, 1, 1]
    ]

    board1 = Board(board=b1)
    winner1 = Board.check_winner(board1)
    assert winner1 == -1


def test_columns():
    b1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 2, 1, 0, 0, 0],
        [0, 2, 1, 1, 2, 1, 2],
        [0, 1, 2, 1, 2, 1, 1]
    ]

    board1 = Board(board=b1)
    winner1 = Board.check_winner(board1)
    assert winner1 == 1


def test_rows():
    b1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 1, 2, 1, 0, 0, 0],
        [0, 2, 1, 1, 1, 1, 2],
        [0, 1, 2, 1, 2, 1, 1]
    ]

    board1 = Board(b1)
    winner1 = Board.check_winner(board1)
    assert winner1 == 1


def test_diagonal_left_to_right():
    # winner 1 (1st diagonal)
    b1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 2, 0, 0, 0],
        [2, 1, 2, 1, 0, 0, 0],
        [1, 2, 1, 2, 1, 1, 2],
        [2, 1, 2, 1, 2, 1, 1]
    ]

    # winner 2 (2nd diagonal)
    b2 = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 2, 0, 1, 0, 0, 0],
        [2, 1, 2, 1, 0, 0, 0],
        [1, 2, 2, 2, 1, 1, 2],
        [2, 1, 2, 1, 2, 1, 1]
    ]

    board1 = Board(b1)
    winner1 = Board.check_winner(board1)
    assert winner1 == 1

    board2 = Board(b2)
    winner2 = Board.check_winner(board2)
    assert winner2 == 2


def test_diagonal_right_to_left():
    # winner 1 (1st diagonal)
    b1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [2, 1, 2, 1, 0, 1, 2],
        [1, 2, 1, 2, 1, 1, 2],
        [2, 1, 2, 1, 2, 1, 1]
    ]

    # winner 2 (4th diagonal)
    b2 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 2, 0, 0, 2],
        [2, 1, 2, 1, 2, 1, 1],
        [1, 2, 2, 2, 1, 1, 2],
        [2, 1, 1, 1, 2, 1, 1]
    ]

    board1 = Board(b1)
    winner1 = Board.check_winner(board1)
    assert winner1 == 1

    board2 = Board(b2)
    winner2 = Board.check_winner(board2)
    assert winner2 == 2


def test_play_turn():
    b = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 0],
        [0, 2, 1, 2, 0, 0, 0],
        [0, 1, 2, 1, 2, 1, 1]
    ]

    board = Board(board=np.array(b), turn=2)
    winner_before = Board.check_winner(board)

    assert winner_before == -1
    assert board.terminal is False

    new_board = board.play_turn(1)

    assert new_board.winner == 2
    assert new_board.terminal is True


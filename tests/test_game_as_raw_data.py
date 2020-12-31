from monte_carlo.board import Board


def test_board_as_string():
    board = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 2, 0, 2, 2, 0, 0],
        [0, 1, 0, 1, 1, 2, 0],
        [0, 1, 0, 2, 2, 1, 0],
        [2, 1, 1, 1, 2, 1, 0],
        [1, 2, 1, 2, 2, 1, 2]
    ]

    board = Board(board=board, turn=1)
    assert board.__str__() == "000200002022000101120010221021112101212212" + str(board.turn)




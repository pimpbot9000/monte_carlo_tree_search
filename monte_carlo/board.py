from copy import copy, deepcopy
import random
import numpy as np


class Board:
    WIN = 4
    cols = 7
    rows = 6

    def __init__(self, board=None, turn=1, previous_move=-1, terminal=False, winner=-1):
        """
        :param board:
        :param turn: Whose turn it's to play next (1 or 2)
        :param previous_move: Move that lead to this position (0-6).
        """
        if board is None:
            self.board = np.full((6, 7), 0)
            self.turn = 1
        elif type(board) == np.ndarray:
            self.turn = turn
            self.board = board
        elif type(board) == list:
            self.turn = turn
            self.board = np.array(board)
        else:
            raise Exception("Board is invalid type")

        self.previous_move = previous_move
        self.terminal = terminal
        self.winner = winner

    @staticmethod
    def check_winner(board_obj):

        nof_pieces = board_obj.count_pieces()
        board = board_obj.board

        if nof_pieces < 2 * Board.WIN - 1:
            return -1

        # check columns
        board_ud = np.flipud(board)
        for col_index in range(0, Board.cols):
            col = board_ud[:, col_index]
            result = Board.check_sequence(col, True)
            if result != 0:
                return result

        # check rows
        for row_index in range(0, Board.rows):
            row = board_ud[row_index, :]
            result = Board.check_sequence(row)
            if result != 0:
                return result

        # check diagonal: left to right
        for offset in range(-2, 4):
            diagonal = np.diag(board, offset)
            result = Board.check_sequence(diagonal)
            if result != 0:
                return result

        # check diagonal: right to left
        board_lr = np.fliplr(board)
        for offset in range(-2, 4):
            diagonal = np.diag(board_lr, offset)
            result = Board.check_sequence(diagonal)
            if result != 0:
                return result

        if nof_pieces == Board.cols*Board.rows:
            return 0  # draw
        else:
            return -1  # not finished

    @staticmethod
    def check_sequence(seq, terminate_on_zero=False):
        seq = seq.tolist() # for faster iteration
        current = None
        counter = 0

        for value in seq:
            if value == 0:
                if terminate_on_zero:
                    return 0
                current = 0
                counter = 0
            elif value == current:
                counter += 1
            elif value != current:
                current = value
                counter = 1

            if counter == Board.WIN:
                return current

        return 0

    def play_turn(self, move):
        """
        :param move: column index where the piece is "dropped"
        :return: returns a new Board object
        """
        if self.terminal:
            raise Exception("The game is in terminal state. Cannot continue.")

        board = np.copy(self.board)
        col = np.flip(board[:, move]).tolist()

        index = col.index(0)

        board[self.rows - 1 - index][move] = self.turn

        new_player = 1 if self.turn == 2 else 2

        board_obj = Board(board, turn=new_player, previous_move=move)
        winner = Board.check_winner(board_obj)

        if winner != -1:
            board_obj.terminal = True
            board_obj.winner = winner

        return board_obj

    def possible_moves(self):
        top_row = self.board[0]
        moves = []
        for index, value in enumerate(top_row):
            if value == 0:
                moves.append(index)
        return moves

    def count_pieces(self):
        return np.count_nonzero(self.board)

    def previous_turn(self):
        if self.count_pieces() == 0:
            return 0
        elif self.turn == 1:
            return 2
        else:
            return 1

    def print_board_info(self):
        print("turn:", self.turn)
        print("possible moves", self.possible_moves())
        print("previous turn", self.previous_turn())
        print("previous move", self.previous_move)
        print("terminal", self.terminal)
        print("winner", self.winner)

    def print_board(self):

        def print_horizontal_line():
            print((4*Board.cols + 1)*"-")

        print_horizontal_line()
        for row in range(0, Board.rows):
            row_str = "|"
            row = self.board[row, :]
            for piece in row:
                if piece == 0:
                    row_str += "   |"
                else:
                    row_str += " " + str(piece) + " |"
            print(row_str)
            print_horizontal_line()

        row_str = " "
        for i in range(0, Board.cols):
            row_str += " " + str(i) + "  "
        print(row_str)

    @staticmethod
    def simulate(board):
        """
        :param board: Board
        :return: 0 = draw, 1 = Player 1 wins, 2 = Player 2 wins
        """
        winner = -1

        while winner == -1:
            moves = board.possible_moves()
            move = random.choice(moves)
            board = board.play_turn(move)
            winner = Board.check_winner(board_obj=board)
        #board.print_board_info()
        #board.print_board()
        return winner









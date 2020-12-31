import random
import math
from typing import List
from monte_carlo.board import Board
from functools import cmp_to_key
from copy import copy


class Minimax:
    def __init__(self, max_depth=10, verbose=True):
        self.MAX_DEPTH = max_depth
        self.random_move = True
        self.discount = 0.95  # This is an arbitrary number that satisfy cond. 0 < discount < 1
        self.verbose = verbose

    def minimax(self, board: Board, alpha, beta, is_maximizing_player, player, depth):

        if board.terminal:
            if board.winner == 0:
                return 0, -1
            elif board.winner != player:
                return -1 * (self.discount ** depth), -1  # value, move
            elif board.winner == player:
                return 1 * (self.discount ** depth) , -1   # value, move

        moves = board.possible_moves()

        if depth == self.MAX_DEPTH:
            return 0, -1

        if len(moves) == 0:  # probably no necessary
            return 0, -1

        if is_maximizing_player:
            max_eval = -math.inf
            optimal_move = -1
            pos_moves = board.possible_moves()

            new_boards = [board.play_turn(move) for move in pos_moves]
            new_boards = self.sort_boards(new_boards, board.turn, board.count_pieces(), self.random_move)
            for new_board in new_boards:

                _eval, _ = self.minimax(new_board, alpha, beta, False, player, depth+1)
                if _eval > max_eval:
                    max_eval = _eval
                    optimal_move = new_board.previous_move  # previous move led to this state

                alpha = max(alpha, _eval)

                if beta <= alpha:
                    break

            return max_eval, optimal_move

        else:
            min_eval = math.inf
            optimal_move = -1
            pos_moves = board.possible_moves()

            new_boards = [board.play_turn(move) for move in pos_moves]
            new_boards = self.sort_boards(new_boards, board.turn, board.count_pieces(), self.random_move)

            for new_board in new_boards:
                _eval, m = self.minimax(new_board, alpha, beta, True, player, depth+1)
                if _eval < min_eval:
                    min_eval = _eval
                    optimal_move = new_board.previous_turn()

                beta = min(beta, _eval)

                if beta <= alpha:
                    break

            return min_eval, optimal_move

    def search(self, board: Board):
        if self.verbose:
            print("Minimax searching...")

        value, move = self.minimax(board, -1, 1, True, board.turn, 0)

        if self.verbose:
            print("value:", value, ", Move:", move)

        return move

    @staticmethod
    def sort_boards(boards: List[Board], player, turns_played, random_move):
        if random_move and turns_played < 15:
            new_boards = copy(boards)
            random.shuffle(new_boards)
            return new_boards
        else:
            boards = sorted(boards, key=cmp_to_key(Minimax.make_comparator(player)))
            return boards

    @staticmethod
    def make_comparator(player):
        def compare(b1: Board, b2: Board):
            if player == 1 and (b1.winner == 1 and b2.winner == 2 or b1.winner == 2 and b2.winner == 1):
                return b1.winner - b2.winner
            else:
                return b2.winner - b1.winner
        return compare








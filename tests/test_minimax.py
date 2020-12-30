from monte_carlo.minimax import Minimax


def test_sorting():

    class DummyBoard:
        def __init__(self, name, winner):
            self.name = name
            self.winner = winner

        def __str__(self):
            return "name: {name}, winner: {winner}".format(name=self.name, winner=self.winner)

    boards = [
        DummyBoard("a", 1),
        DummyBoard("b", 2),
        DummyBoard("c", -1),
        DummyBoard("d", 0),
        DummyBoard("e", 1),
        DummyBoard("f", 2),
        DummyBoard("g", 1),
        DummyBoard("h", 1),
        DummyBoard("i", 2),

    ]
    m = Minimax()
    # Note: moves are randomized when turns_played < 10
    boards = m.sort_boards(boards, player=1, turns_played=15, random_move=False)
    winners = [b.winner for b in boards]
    assert [1, 1, 1, 1, 2, 2, 2, 0, -1] == winners

    boards = m.sort_boards(boards, player=2, turns_played=15, random_move=False)
    winners = [b.winner for b in boards]
    assert [2, 2, 2, 1, 1, 1, 1, 0, -1] == winners


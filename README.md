# Connect Four - The AI

## Motivation
Last Christmas my sister's 9 yo daughter beat me in *Connect Four* multiple times in a row (no pun intended). To find some spiritual redemption I explored (and exploited!) some tree search algorithms to beat the game (or at least to help me beat children ... i'm not a nice guy).

![](https://upload.wikimedia.org/wikipedia/en/7/79/Connect_4_Board_and_Box.jpg)

## Minimax
Initially I implemented an AI based on the *minimax algorithm*. It turned out that minimax - being essentially a brute force method - was very slow... even with alpha-beta pruning. Who could have guessed!
(According to [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)  there are 4,531,985,219,092 board positions).

### Not all wins or losses are born equal
I noticed that with minimax if all wins are of value 1 and losses of value -1, when the minimax notices that it's going to win/lose eventually no matter what, it did not care anymore which losing move to play (i.e. it could play a move the caused it to lose immediately next turn instead of playing a move that would have lead to defeat in 6 moves).

That's quite poor sportsmanship so losses/wins are discounted taking into account the depth.

In essence taking the discounted value of win/loss score minimax is going to choose the shortest path to victory (instead of screwing around with it's opponent) or the longest path to loss ... you never know if the opponent (human or Monte Carlo Tree Search) is going to make a mistake! It ain't over 'till the fa ... ahem, the curvy lady sings.

## Monte Carlo Tree Search (MCTS)

Nothing special here. A "vanilla MCTS" using something called *Upper Confidence Bound 1 applied to trees*(?) for the exploration/exploitation balance. See [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation) for "more" details. The simulations are ran all the way down to a terminal state (win/loss/draw) and the scores are back propagated all the way to the root ... taking into account the maximizing and minimizing player.

##  All non-terminal states are born equal

If the game is not in terminal state (win/loss/draw) I did not implement any method to evaluate the board position. I guess the fancy way to say is there is no domain-specific expert knowledge and/or both algorithms are domain agnostics.

### The downfall of Minimax

With any timewise sensible search depth (~10) and without any way to evaluate non-terminal board positions/moves the Minimax has no way to know which is a *good* play in the beginning of the game. In essence Minimax only knows which plays are *bad* i.e which plays are going to lead to an inevitable loss in the next ~10 (= *search depth*) turns (assuming that the opponent is playing an optimal game). Sure the Minimax finds always a path to victory - if there is one - in the end game but it's a cold comfort if more aggressive opponent at least had some clue what is a good strategy in the beginning.

This said, in a game of MCTS vs. Minimax, MCTS wins virtually every time since MCTS is more aggressive - trying to win instead of not trying to lose. The MCTS algorithm has some sense of a good strategy in the beginning of the game.

There are rare occasions when MCTS loses: the MCTS does not guarantee it finds the best strategy. If the stars are aligned in some funny way MCTS might pick a "wrong" path which seemingly leads to victory and snowball-exploit it without exploring other possibilities properly, or some branch which seemingly leads to a loss is pruned out. In the latter case an expert player (in this case mr. Minimax) might be able to exploit this branch and find a path to victory.

#### Fun fact

MCTS starts the game virtually every time by placing a piece in the middle column. This is considered to be a best strategy for the starting player according to human intuition and mathemagicians. According to [Wikipedia](https://en.wikipedia.org/wiki/Connect_Four#Mathematical_solution) it is objectively the best play: "*The solved conclusion for Connect Four is first player win.*"

## Running the application

Playing human vs. AI (MCTR):
```
python main.py human
```

The ultimate duel: AI vs. AI (MCTS vs. Minimax):
```
python main.py ai
```
I was planning to add command line arguments to set the search depth (Minimax) and number of simulations (MCTS) but I was to lazy.

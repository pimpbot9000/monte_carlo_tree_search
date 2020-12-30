# Connect four - The AI

## Motivation
Last Christmas my sister's 9 yo daughter beat me in 4 in a Row game multiple times.
To find some spiritual redemption I had to code an AI to beat the game (or help me beat children).

![](https://upload.wikimedia.org/wikipedia/en/7/79/Connect_4_Board_and_Box.jpg)

## Minimax
Initially I implemented an AI based on minimax algorithm. It turned out that Minimax - being essentially a brute force method - was very slow... even with alpha-beta pruning. Who could have guessed!
(According to [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)  there are 4,531,985,219,092 board positions).

### Not all wins or losses are born equal
I noticed that with minimax if all wins are of value 1 and losses of value -1, when the minimax notices that it's going to win/lose eventually no matter what, it did not care anymore which losing move to play (it could play a move the caused it to lose immediately instead of playing a move that would have lead to defeat in 6 moves).

That's quite poor sportsmanship so losses/wins are discounted taking into account the depth.

In essence taking the discounted value of win/loss score minimax is going to choose the shortest path to victory (instead of screwing around with opponent) or the longest path to loss ... you never know if the opponent (human or Monte Carlo Tree Search) is going to make a mistake! Last man standing!


## Monte Carlo Tree Search (MCTS)

Nothing special here. A "vanilla MCTS" using something called "Upper Confidence Bound 1 applied to trees"(?). See [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation) for details. The simulations are ran all the way down to terminal state (win/loss/draw) and the scores are back propagated all the way to the root ... taking into account the maximizing and minimizing player.

##  All non-terminal states are born equal

If the game is not in terminal state (win/loss/draw) there's no method to valuate the state. I guess the fancy way to say is there is no domain-specific expert knowledge and both algorithms are domain agnostics.

## Running the application

Playing human vs. AI (MCTR):
```
python main.py human
```

The ultimate duel: AI vs. AI (MCTS vs. Minimax):
```
python main.py ai
```
I was planning to add command line arguments to set the search depth (Minimax) and number of simulations (MCTS) but got bored.

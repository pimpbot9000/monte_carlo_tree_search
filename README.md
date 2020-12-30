# Connect Four - The "AI"

## Motivation
Christmas of twenty-twenty my 9 yo niece beat me in *Connect Four* multiple times in a row (no pun intended). To find some spiritual redemption I explored (and exploited! Yes, pun intended) some tree search algorithms to beat the game (or at least to help me beat my niece ... I'm not a nice guy).

![](https://upload.wikimedia.org/wikipedia/en/7/79/Connect_4_Board_and_Box.jpg)

## Minimax
Initially I implemented game tree search based on the *minimax algorithm*. It turned out that minimax - being essentially a brute force method - was very slow... even with alpha-beta pruning. Who could have guessed!
(According to [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)  there are 4,531,985,219,092 board positions).

### Not all wins or losses are born equal
I noticed that with minimax if all wins are of value 1 and losses of value -1 no matter the depth, when the minimax notices that it's going to lose eventually no matter what, it did not care anymore which losing move to play (i.e. it could play a move the caused it to lose immediately next turn instead of playing a move that would have lead to defeat in say, 6 moves). Same happened when minimax saw multiple paths to a definite victory. It did not care at all to let the opponent out of it's misery as soon as possible. It's quite fun experience to realise that the algorithm you just implemented turns out to be a ... dick.

That's quite poor sportsmanship so losses/wins are discounted taking into account the depth.

In essence taking the discounted value of win/loss score minimax is going to choose the shortest path to victory (instead of screwing around with it's opponent) and the longest path to loss ... which is a good strategy since you never know if the opponent is going to make a mistake. It ain't over 'till the fa ... ahem, the curvy lady sings!

## Monte Carlo Tree Search (MCTS)

Nothing special here. A "vanilla" MCTS using something called *Upper Confidence Bound 1 applied to trees* (?) for the exploration/exploitation balance. See [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation) for more details. The simulations are ran all the way down to a terminal state (win/loss/draw) and the scores are back propagated and stuff ... taking into account the maximizing and minimizing player.

##  All non-terminal states are born equal

If the game is not in terminal state (win/loss/draw) I did not implement any method to evaluate the board position. I guess the fancy way to say this is that there is no domain-specific knowledge and/or both algorithms are domain agnostics.

## The Downfall of Minimax

With any timewise sensible search depth (~10) and without evaluation of the non-terminal board positions/moves the Minimax has no way to know which is a *good* play in the beginning of the game. In essence Minimax only knows which plays are *bad* i.e which plays are going to lead to an inevitable loss in the next ~10 turns (assuming that the opponent is playing an optimal game). Sure the Minimax finds always a path to victory - if there is one - in the end game but it's a cold comfort if more aggressive opponent at least had some clue what is a good strategy in the very beginning.

This said, in a game of MCTS vs. Minimax, MCTS wins virtually every time since MCTS is more aggressive - trying to win instead of just not trying to lose. The MCTS algorithm has some sense of a good strategy in the beginning of the game.

## The Shortcomings of the MCTS
There are some rare occasions when MCTS loses against Minimax: the MCTS does not guarantee it finds the best strategy. If the stars of pseudo random generators are aligned in some weird way MCTS might pick a "wrong" path which seemingly leads to victory and snowball-exploit it without exploring other possibilities properly, or some branch which seemingly leads to a loss is left unexplored. In the latter case opponent might be able to exploit this branch and find a path to Glorious Victory!!

I deeply think that there's is a lesson here for us humans to learn.

#### Fun fact

As it happens, MCTS starts the game virtually every time by placing a piece in the middle column. This is considered to be a best strategy for the starting player according to human intuition, experience and mathemagicians. According to [Wikipedia](https://en.wikipedia.org/wiki/Connect_Four#Mathematical_solution) it is *objectively* the best play: "*The solved conclusion for Connect Four is first player win. With perfect play, the first player can force a win \[...\] starting in the middle column.*". I take this as a proof that my MCTS implementation is doing something rite.

## Running the application

Playing human vs. AI (MCTS):
```
python main.py human
```

The ultimate duel: AI vs. AI (MCTS vs. Minimax):
```
python main.py ai
```
I was planning to add command line arguments to set the search depth (Minimax) and number of simulations (MCTS) but I was too lazy.

Oh, there's a text based UI. Have fun.

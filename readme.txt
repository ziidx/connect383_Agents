Jack DeGuglielmo, George Chiang
Bot Name: WHEEZY
Our design for the evaluation function consists of a for loop that iterates through each cell in a state. If the cell is surrounded by an adjacent cell of the same player, 
a point is added. Although our heuristic only considers pairs, we believe that the number of adjacent matches could be correlated with success of a game.

Choose_Middle: This board tests if player 1 will choose the middle column or far right column as its first move. Although both moves are good moves, the middle column should
be chosen since it provides a far greater utility value compared to the right column.

Choose_Middle 2: This board tests if player 1 will choose the middle column or middle left column. On the surface, picking middle left appears to be better because it blocks
a 4 streak for player 2. However, the correct move should be to pick the middle column because the total score for player 1 would come out higher even if player 2 gets the 4
streak. In other words, the middle column allows player 1 to win even if the middle left column appears to be of higher utility.

Small_right: Small right always results in a tie. Whether player 1 blocks player 2's three in a row or takes its own, the outcome is the same. 
This tests how our algorithm selects an even util move. Because we use the first best util successor, Player 1 chooses left.
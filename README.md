# 21/Blackjack-game

From a single deck of cards: pick two for the player and two for the house. Show the player's cards.
Calculate the total score. Ask if they want another card, unless the score is 21. Please note that the Ace can be 1 or 11. Ace + Queen = 21 points (the Ace is 11 points). Ace + Queen + Jack = 21 points (the Ace is 1 point). In your first version, you could set Ace to either 1 or 11 (but make sure to let the player know).
Use a simple algorithm to do the same for the house. You could do this randomly or come up with a simple rule. If the total score of the house is greater than or equal to that of the player, the house wins. 
Otherwise, the player wins. E.g., if both the player and the house of 20 points, the house wins.
Naturally, any score over 21 means that player is bust and loses.

Example

Player: 
- 10 of hearts
- 8 of clubs

Program : Hit or Stay?
Player  : H
Program : 3 of diamonds (total points is now 21)

Program:
- 7 of hearts
- 3 of clubs
- 10 of spades (20 points)

If the program stops, the player has won. This is probably the smartest thing to do, as the chance of getting an Ace is actually very small.


# Dominion Game:

This a project for the creation of a program that can execute the rules for the board game dominion. Currently, I am creating a system that can allow for the playing of the game of Dominion, with the intention of eventually creating Dominion playing bots.

Currently the engine works, but I don't have a usable agent constructed for learning. The issue is that creating a system to meaningfully evaluate the current board state and provide reward based on the move taken is proving challenging.


## Structure of the Engine:


As it stands most aspects of the game are divided into classes. The game itself exists as a class and contains a store class as well as a Player class object. Each player has their own deck, discard and hand class objects and can manipulate them using various objects.


Players also contain most of the functions including drawing cards, discarding cards, shuffling their decks and playing cards. As most of the cards modify the player's current attributes this option seems like the best arrangement.


The cards file contains the Card class and all of the cards currently implemented. Each card object contains all standard game values and attributes. Cards also have a special features marker. This is referenced by the play function in the Dominion file and is intended to handle cards with non-standard effects. The early vs. after distinction in the special handles situations where card effects will happen before or after the standard card text.


## Turn Structure

A game is instatiated with a list of player objects. When the play game function is run, the game removes the first player in the player list, runs the take turn function (which varies from bot/real player) and then puts the player on the back of the player list. This process continues until the Game End function is true, at which point each player object calculates VPs (using their inherent function) and the winner is determined.
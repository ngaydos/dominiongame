# Dominion Game:

This a project for the creation of a program that can execute the rules for the board game dominion. Currently, I am creating a system that can allow for the playing of the game of Dominion, with the intention of eventually creating Dominion playing bots.

Currently the engine works, but I don't have a usable agent constructed for learning.


## Structure of the Engine


As it stands most aspects of the game are divided into classes. The game itself exists as a class and contains a store class as well as a Player class object. Each player has their own deck, discard and hand class objects and can manipulate them using various objects.
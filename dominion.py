import random

class Game:

    def __init__(self, player_count):
        self.player_count = player_count


class Player:

    def __init__(self):
        self.hand = Hand()
        self.deck = Deck()
        self.discard = Discard()
        self.vps = None

    def draw(self, count = 1):
        if len(self.deck.cards) < count:
            remaining = count - len(self.deck.cards)
            self.draw(len(self.deck.cards))
            if len(self.discard.cards) < remaining:
                self.shuffle()
                self.draw(len(self.deck.cards))
            else:
                self.shuffle()
                self.draw(remaining)
        else:
            for val in range(count):
                card = random.choice(self.deck.cards)
                self.hand.cards.append(card)
                self.deck.cards.remove(card)

    def shuffle(self):
        self.deck.cards += self.discard.cards
        self.discard.cards = []


    def discard_hand(self):
        self.discard.cards += self.hand.cards
        self.hand.cards = []

class Deck:

    def __init__(self):
        self.cards = [Card('copper', ['money'], 0, 0, 0, 1), Card('copper', ['money'], 0, 0, 0, 1), Card('copper', ['money'], 0, 0, 0, 1), Card('copper', ['money'], 0, 0, 0, 1),
         Card('copper', ['money'], 0, 0, 0, 1), Card('copper', ['money'], 0, 0, 0, 1), Card('copper', ['money'], 0, 0, 0, 1), 
         Card('estate', ['victorypoint'], 2, 0, 0, 0, 1), Card('estate', ['victorypoint'], 2, 0, 0, 0, 1), Card('estate', ['victorypoint'], 2, 0, 0, 0, 1)]

    def __call__(self):
        return [card.name for card in self.cards]


class Hand:
    
    def __init__(self):
        self.cards = []

    def __call__(self):
        return [card.name for card in self.cards]

class Discard:

    def __init__(self):
        self.cards = []

    def __call__(self):
        return [card.name for card in self.cards]

class Card:

    def __init__(self, name, ctypes, cost, actions, draw, gold, vps =0):
        self.name = name
        self.ctypes = ctypes
        self.cost = cost
        self.actions = actions
        self.draw = draw
        self.gold = gold
        self.vps = vps

    def __call__(self):
        return self.name

#Structural Notes:

'''You could set up a card as a class containing data on cost, name, vps and possibly type. 
This makes playing the cards easier but generates some issues. Alternately you could go with the less
systemic option and generate a specific function response for each card.

I think to be able to use a machine learning system each card is going to need to be an instance of a card class.'''


import random
from collections import deque

class Game:

    def __init__(self, players):
        #players is a list of player objects
        self.player_count = len(players)
        self.store = Store()
        self.players = deque(players)

    def play_game(self):
        while province in self.store:
            current_player = self.players.popleft()
            #take turn here
            self.players.append(current_player)

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
        self.cards = [copper, copper, copper, copper, copper, copper, copper, estate, estate, estate]

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
        #card types as a list allows for the multiple card types introduced in intrigue
        self.ctypes = ctypes
        self.cost = cost
        self.actions = actions
        self.draw = draw
        self.gold = gold
        self.vps = vps

    def __call__(self):
        return self.name

copper = Card('copper', ['money'], 0, 0, 0, 1)
silver = Card('silver', ['money'], 3, 0, 0, 2)
gold = Card('gold', ['money'], 6, 0, 0, 3)
estate = Card('estate', ['victorypoint'], 2, 0, 0, 0, 1)
duchy = Card('duchy', ['victorypoint'], 5, 0, 0, 0, 3)
province = Card('province', ['victorypoint'], 8, 0, 0, 0, 6)

class Store:
    pass


#Structural Notes:

'''You could set up a card as a class containing data on cost, name, vps and possibly type. 
This makes playing the cards easier but generates some issues. Alternately you could go with the less
systemic option and generate a specific function response for each card.


'''
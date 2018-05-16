import random
from collections import deque

class Game:

    def __init__(self, players):
        #players is a list of player objects
        self.player_count = len(players)
        self.store = create_store()
        self.players = deque(players)

    def play_game(self):
        while province in self.store:
            current_player = self.players.popleft()
            current_player.take_turn(self)
            self.players.append(current_player)
        final_scores = [player.calculate_vps() for player in self.players]
        return (self.players, final_scores)


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

    def take_turn(self, game):
        money_count = 0
        for card in self.hand.cards:
            #eventually there should be a play function
            #eventually buy needs to check if the card is in the store rather than checking in this automated function
            money_count += card.money
            self.hand.discard(card, self.discard)
        if money_count >= 8:
            self.buy(province, game.store)
        elif money_count >= 6 and gold in game.store:
            self.buy(gold, game.store)
        elif money_count >= 5 and duchy in game.store:
            self.buy(duchy, game.store)
        elif money_count >= 3 and silver in game.store:
            self.buy(silver, game.store)
        elif money_count >= 2 and estate in game.store:
            self.buy(estate, game.store)
        else:
            self.buy(copper, game.store)
        self.discard_hand()
        self.draw(5)

    def buy(self, card, store):
        #for now this function is simple but it eventually needs to be capable of checking if the card is in the store
        #and check if the player has the available gold, manage the number of buys
        #also you need a gain function eventually which would be similar, but work without caring about those things
        if card in store:
            self.discard.cards.append(card)
            store.remove(card)

    def calculate_vps(self):
        vpcount = 0
        for card in self.hand.cards:
            vpcount += card.vps
        for card in self.discard.cards:
            vpcount += card.vps
        for card in self.deck.cards:
            vpcount += card.vps
        return vpcount


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

    #eventually this should be handled as a play function
    def discard(self, card, discard_pile):
        discard_pile.cards.append(card)
        self.cards.remove(card)



class Discard:

    def __init__(self):
        self.cards = []

    def __call__(self):
        return [card.name for card in self.cards]

class Card:

    def __init__(self, name, ctypes, cost, actions, draw, money, vps =0):
        self.name = name
        #card types as a list allows for the multiple card types introduced in intrigue
        self.ctypes = ctypes
        self.cost = cost
        self.actions = actions
        self.draw = draw
        self.money = money
        self.vps = vps

    def __call__(self):
        return self.name

copper = Card('copper', ['money'], 0, 0, 0, 1)
silver = Card('silver', ['money'], 3, 0, 0, 2)
gold = Card('gold', ['money'], 6, 0, 0, 3)
estate = Card('estate', ['victorypoint'], 2, 0, 0, 0, 1)
duchy = Card('duchy', ['victorypoint'], 5, 0, 0, 0, 3)
province = Card('province', ['victorypoint'], 8, 0, 0, 0, 6)


def create_store():
    store = []
    for i in range(12):
        store.append(estate)
        store.append(duchy)
        store.append(province)
    for i in range(20):
        store.append(copper)
        store.append(silver)
        store.append(gold)
    return store
#Structural Notes:

'''You could set up a card as a class containing data on cost, name, vps and possibly type. 
This makes playing the cards easier but generates some issues. Alternately you could go with the less
systemic option and generate a specific function response for each card.


'''
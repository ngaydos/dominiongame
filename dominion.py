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
            if len(self.discard.cards) < count:
                self.shuffle()
                self.draw(len(deck.cards))
            else:
                self.shuffle()
                self.draw(remaining)
        else:
            card = random.choice(self.deck.cards)
            self.hand.cards.append(card)
            self.deck.cards.remove(card)

    def shuffle(self):
        self.deck.cards.append(self.discard.cards)
        self.discard.cards = []

class Deck:

    def __init__(self):
        self.cards = ['copper', 'copper', 'copper', 'copper', 'copper', 'copper', 'copper', 'estate', 'estate', 'estate']



class Hand:
    
    def __init__(self):
        self.cards = []

class Discard:

    def __init__(self):
        self.cards = []
class Game:

    def __init__(self, player_count):
        self.player_count = player_count


class Player:

    def __init__(self):
        self.hand = Hand()
        self.deck = Deck()
        self.vps = None

class Deck:

    def __init__(self):
        self.cards = ['copper', 'copper', 'copper', 'copper', 'copper', 'copper', 'copper', 'estate', 'estate', 'estate']



class Hand:
    
    def __init__(self):
        self.cards = []


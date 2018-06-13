from dominion import *

class Big_Money_Bot:
    
    def __init__(self, is_bot = True):
        self.hand = Hand()
        self.deck = Deck()
        random.shuffle(self.deck.cards)
        self.discard = Discard()
        self.is_bot = is_bot
        self.vps = None
        self.current_money = 0
        self.draw(5)
        self.available_actions = 0
        self.available_buys = 0
        self.play_area = []


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
                #pop at -1 because it removes the leftmost element. Means that appending items puts them on the bottom of the deck.
                card = self.deck.cards.pop(-1)
                self.hand.cards.append(card)

    def shuffle(self):
        self.deck.cards += self.discard.cards
        random.shuffle(self.deck.cards)
        self.discard.cards = []


    def discard_hand(self):
        self.discard.cards += self.hand.cards
        self.hand.cards = []

    def take_turn(self, game, bot_player):
        self.available_actions = 1
        self.available_buys = 1
        for card in self.hand.cards:
            self.play(card, game)
        if self.current_money >= 8:
            self.buy(province, game.store)
        elif self.current_money >= 6 and gold in game.store:
            self.buy(gold, game.store)
        elif self.current_money >= 3 and silver in game.store:
            self.buy(silver, game.store)
        self.end_turn()


    def end_turn(self):
        self.discard_hand()
        self.current_money = 0
        self.available_actions = 0
        self.discard.cards += self.play_area
        self.play_area = []
        self.draw(5)

    def play(self, card, game):
        '''
        plays a card. This process handles all the general rules i.e.
        +actions, +money, +draw, +buy (not yet, but it will)
        any special factors in the action card get fed to the play_special function
        inputs: a card object, a game object
        outputs: none
        '''
        if 'action' in card.ctypes:
            if self.available_actions <= 0:
                print('out of actions')
                return None
            else:
                self.available_actions -= 1
        if card.special == 'early':
            self.play_special(card, game)
        self.draw(card.draw)
        self.current_money += card.money
        self.available_actions += card.actions
        self.available_buys += card.buys
        if card.special == 'after':
            self.play_special(card, game)
        self.play_area.append(card)
        self.hand.cards.remove(card)

    def play_special(self, card, game):
        if card.name == 'council room':
            for player in game.players:
                player.draw(1)
        if card.name == 'witch':
            for player in game.players:
                player.gain(curse)

    def buy(self, card, store):
        #checks if the player has available buys and if the card selected is in the store
        #needs to check the play has enough gold
        if card in store and self.available_buys >= 1 and self.current_money >= card.cost:
            self.discard.cards.append(card)
            store.remove(card)
            self.available_buys -= 1
            self.current_money -= card.cost
        elif card not in store:
            return "card not in store"
        elif self.available_buys < 1:
            return "no buys available"
        elif self.current_money < card.cost:
            return "not enough money"

    def gain(self, card, store):
        #need to figure out how to deal wiht special cards outside the store that can be gained from elsewhere
        #this will resolve the gaining required for witch
        if card in store:
            self.discard.cards.append(card)
            store.remove(card)
        elif card not in store:
            return "card not in store"

    def calculate_vps(self):
        vpcount = 0
        #card count and gardens count accomodate for gardens if a bit uncleanly
        card_count = 0
        gardens_count = 0
        for card in self.hand.cards:
            vpcount += card.vps
            card_count += 1
            if card.name == 'gardens':
                gardens_count += 1
        for card in self.discard.cards:
            vpcount += card.vps
            card_count += 1
            if card.name == 'gardens':
                gardens_count += 1
        for card in self.deck.cards:
            vpcount += card.vps
            card_count += 1
            if card.name == 'gardens':
                gardens_count += 1
        vpcount += ((card_count//10) * gardens_count)
        return vpcount
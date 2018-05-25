import random
from collections import deque
from cards import *

class Game:

    def __init__(self, players):
        #players is a list of player objects
        self.player_count = len(players)
        self.store = create_store()
        self.players = deque(players)
        self.store_items = set(self.store)

    def play_game(self):

        while self.game_over() == False:
            #iterates through players one at a time until game_over == True
            current_player = self.players.popleft()
            #any bots should have a take turn function to enable them to interact with the game and make them modular
            current_player.take_turn(self, current_player.is_bot)
            self.players.append(current_player)
        final_scores = [player.calculate_vps() for player in self.players]
        return (self.players, final_scores)

#possible structure is while game_over() == False and then have game_over check if provinces are gone. Need to check how

    def game_over(self):
        if province not in self.store:
            return True
        else:
            missing_items = 0
            for item in self.store_items:
                if item not in self.store:
                    missing_items += 1
            if missing_items >= 3:
                return True
        return False


class Player:

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
        if bot_player:
            for card in self.hand.cards:
                self.play(card, game)
            #eventually buy needs to check if the card is in the store rather than checking in this automated function
            if self.current_money >= 8:
                self.buy(province, game.store)
            elif self.current_money >= 6 and gold in game.store:
                self.buy(gold, game.store)
            elif self.current_money >= 5 and duchy in game.store:
                self.buy(duchy, game.store)
            elif self.current_money >= 3 and silver in game.store:
                self.buy(silver, game.store)
            elif self.current_money >= 2 and estate in game.store:
                self.buy(estate, game.store)
            else:
                self.buy(copper, game.store)
            self.end_turn()


        else:
            turn_end = False
            while turn_end is False:
                command = input('Type Command:')
                if command == "end turn":
                    self.end_turn()
                    turn_end = True
                elif command == 'hand':
                    print([card.name for card in self.hand.cards])
                elif command == 'discard':
                    print([card.name for card in self.discard.cards])
                elif command == 'current money':
                    print(self.current_money)
                elif command[:4] == 'play':
                    self.play(string_to_card[command[5:]], game)
                elif command[:3] == 'buy':
                    self.buy(string_to_card[command[4:]], game.store)

    def end_turn(self):
        self.discard_hand()
        self.current_money = 0
        self.available_actions = 0
        self.discard.cards += self.play_area
        self.play_area = []
        self.draw(5)

    def play(self, card, game):
        if 'action' in card.ctypes:
            if self.available_actions <= 0:
                print('out of actions')
                return None
            else:
                self.available_actions -= 1
        if card.special == 'early':
            play_special(card.name, self, game)
        self.draw(card.draw)
        self.current_money += card.money
        self.available_actions += card.actions
        if card.special == 'after':
            play_special(card.name, self, game)
        self.play_area.append(card)
        self.hand.cards.remove(card)

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


def create_store():
    store = []
    for i in range(10):
        store.append(village)
        store.append(smithy)
    for i in range(12):
        store.append(estate)
        store.append(duchy)
        store.append(province)
    for i in range(20):
        store.append(copper)
        store.append(silver)
        store.append(gold)
        store.append(curse)
    return store

if __name__ == '__main__':
    #currently requires the commands to be typed in strings
    player1 = Player(is_bot=False)
    player2 = Player()
    player3 = Player()
    game = Game([player1, player2, player3])
    game.play_game()


'''Long term adjustments to be made:

-Play area seems to be working
-Add structure for buys
-Add a buy monitor
    Create an error if the player tries to buy something they can't
    ValueError or not an actual code error, probably not an actual code error.
-Bots
    -Move bots to separate files and then import them as needed, probably can get rid of "is bot" at that point, maybe?
-Structure for cards that are special actions
    Cards now have a special attribute, just need to set up something for a before or after the card since some cards will care about it.
-Trash'''
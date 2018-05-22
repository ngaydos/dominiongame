class Card:

    def __init__(self, name, ctypes, cost, actions, draw, money, buys= 0, vps =0, special = None):
        self.name = name
        #card types as a list allows for the multiple card types introduced in intrigue
        self.ctypes = ctypes
        self.cost = cost
        self.actions = actions
        self.draw = draw
        self.money = money
        self.vps = vps
        self.special = special

    def __call__(self):
        return self.name

copper = Card('copper', ['money'], 0, 0, 0, 1)
silver = Card('silver', ['money'], 3, 0, 0, 2)
gold = Card('gold', ['money'], 6, 0, 0, 3)
estate = Card('estate', ['victorypoint'], 2, 0, 0, 0, vps=1)
duchy = Card('duchy', ['victorypoint'], 5, 0, 0, 0, vps=3)
province = Card('province', ['victorypoint'], 8, 0, 0, 0, vps=6)
curse = Card('curse', ['curse'], 0, 0, 0, 0, vps= -1)
village = Card('village', ['action'], 3, 2, 1, 0)
smithy = Card('smithy', ['action'], 4, 0, 3, 0)
festival = Card('festival', ['action'], 5, 2, 0, 2, buys = 1)
laboratory = Card('laboratory',['action'], 5, 1, 2, 0)
market = Card('market',['action'], 5, 1, 1, 1, buys = 1)

string_to_card = {'copper': copper, 'silver': silver, 'gold': gold, 'estate': estate, 
'duchy': duchy, 'province': province, 'smithy': smithy, 'village': village, 'curse': curse}
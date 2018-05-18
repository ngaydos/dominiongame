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

curse = Card('curse', ['curse'], 0, 0, 0, 0, -1)
copper = Card('copper', ['money'], 0, 0, 0, 1)
silver = Card('silver', ['money'], 3, 0, 0, 2)
gold = Card('gold', ['money'], 6, 0, 0, 3)
estate = Card('estate', ['victorypoint'], 2, 0, 0, 0, 1)
duchy = Card('duchy', ['victorypoint'], 5, 0, 0, 0, 3)
province = Card('province', ['victorypoint'], 8, 0, 0, 0, 6)
village = Card('village', ['action'], 3, 2, 1, 0)
smithy = Card('smithy', ['action'], 4, 0, 3, 0)

string_to_card = {'copper': copper, 'silver': silver, 'gold': gold, 'estate': estate, 
'duchy': duchy, 'province': province, 'smithy': smithy, 'village': village, 'curse': curse}
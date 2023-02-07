#This is strictly a data item. A propert has an owner, number of houses, monopoly status, rent cost, and other such fun.
#Owner will be 0 for bank, 1-8 for P1-P8, and 9 for no owner allowed
#Set will either be "Brown" "Light Blue" "Magenta" "Orange" "Red" "Yellow" "Green" "Blue" "Utility" "Train" "Misc". Misc will do nothing.
#5 Houses  = Hotel

class Property:
    def __init__(self, name, owner, set, price, mortgage, housePrice, houses, rents):
        self.name = name
        self.owner = owner
        self.set = set
        self.price = price
        self.mortgage = mortgage
        self.housePrice = housePrice
        self.houses = houses
        self.rents = rents


#Generate the board being a map of properties to board position.
def generateBoard():
    board = [
        Property("Go", 9, "Misc", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Mediterranean Avenue", 0, "Brown", 60, 30, 50, 0, [2, 10, 30, 90, 160, 250]),
        Property("Community Chest", 9, "Chest", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Baltic Avenue", 0, "Brown", 60, 30, 50, 0, [4, 20, 60, 180, 320, 450]),
        Property("Income Tax", 9, "Tax", 0, 0, 0, 0, [200, 0, 0, 0, 0, 0]),
        Property("Reading Railroad", 0, "Train", 200, 100, 0, 0, [25, 50, 100, 200, 0, 0]),
        Property("Oriental Avenue", 0, "Light Blue", 100, 50, 50, 0, [6, 30, 90, 270, 400, 550]),
        Property("Chance", 9, "Chance", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Vermont Avenue", 0, "Light Blue", 100, 50, 50, 0, [6, 30, 90, 270, 400, 550]),
        Property("Connecticut Avenue", 0, "Light Blue", 120, 50, 60, 0, [8, 40, 100, 300, 450, 600]),
        Property("Jail", 9, "Misc", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("St. Charles Place", 0, "Magenta", 140, 70, 100, 0, [10, 50, 150, 450, 625, 750]),
        Property("Electric Company", 0, "Utility", 150, 75, 0, 0, [4, 10, 0, 0, 0, 0]),
        Property("States Avenue", 0, "Magenta", 140, 70, 100, 0, [10, 50, 150, 450, 625, 750]),
        Property("Virginia Avenue", 0, "Magenta", 160, 80, 100, 0, [12, 60, 180, 500, 700, 900]),
        Property("Reading Railroad", 0, "Train", 200, 100, 0, 0, [25, 50, 100, 200, 0, 0]),
        Property("St. James Place", 0, "Orange", 180, 90, 100, 0, [14, 70, 200, 550, 750, 950]),
        Property("Community Chest", 9, "Chest", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Tennessee Avenue", 0, "Orange", 180, 90, 100, 0, [14, 70, 200, 550, 750, 950]),
        Property("New York Avenue", 0, "Orange", 200, 100, 100, 0, [16, 80, 220, 600, 800, 1000]),
        Property("Free Parking", 9, "Misc", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Kentucky Avenue", 0, "Red", 220, 110, 150, 0, [18, 90, 250, 700, 875, 1050]),
        Property("Chance", 9, "Chance", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Indiana Avenue", 0, "Red", 220, 110, 150, 0, [18, 90, 250, 700, 875, 1050]),
        Property("Illinois Avenue", 0, "Red", 240, 120, 150, 0, [20, 100, 300, 750, 925, 1100]),
        Property("B&O Railroad", 0, "Train", 200, 100, 0, 0, [25, 50, 100, 200, 0, 0]),
        Property("Atlantic Avenue", 0, "Yellow", 260, 130, 150, 0, [22, 110, 330, 800, 975, 1150]),
        Property("Ventnor Avenue", 0, "Yellow", 260, 130, 150, 0, [22, 110, 330, 800, 975, 1150]),
        Property("Water Works", 0, "Utility", 150, 75, 0, 0, [4, 10, 0, 0, 0, 0]),
        Property("Marvin Gardens", 0, "Yellow", 280, 140, 150, 0, [24, 120, 360, 850, 1025, 1200]),
        Property("Go to Jail", 9, "Misc", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Pacific Avenue", 0, "Green", 300, 150, 200, 0, [26, 130, 390, 900, 1100, 1275]),
        Property("North Carolina Avenue", 0, "Green", 300, 150, 200, 0, [26, 130, 390, 900, 1100, 1275]),
        Property("Community Chest", 9, "Chest", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Pennsylvania Avenue", 0, "Green", 320, 160, 200, 0, [28, 150, 450, 1000, 1200, 1400]),
        Property("Short Line", 0, "Train", 200, 100, 0, 0, [25, 50, 100, 200, 0, 0]),
        Property("Chance", 9, "Chance", 0, 0, 0, 0, [0, 0, 0, 0, 0, 0]),
        Property("Park Place", 0, "Blue", 350, 175, 200, 0, [35, 175, 500, 1100, 1300, 1500]),
        Property("Luxury Tax", 9, "Tax", 0, 0, 0, 0, [100, 0, 0, 0, 0, 0]),
        Property("Boardwalk", 0, "Blue", 400, 200, 200, 0, [50, 200, 600, 1400, 1700, 2000])
    ]
    return board

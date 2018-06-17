import pandas as pd
from random import randint

class gaMap():
    def __init__(self):
        filename = 'map ('+ str(randint(0, 10)) +').csv'
        filename = 'map (0).csv'
        self.gaGrid = pd.read_csv('app_resources/maps/'+filename, sep=',',header=None)

    def getCost(self, x,y):
        return int(list(self.gaGrid[x][y])[1])

    def swicz(self, x):
        return {
            'w': 'water',
            'f': 'background_lines',
            'm': 'mountains',
            'b': 'bush',
            's': 'swamp',
        }.get(x, 9) 

    def getFilename(self, x,y):
        symbol = list(self.gaGrid[x][y])[0]
        return self.swicz(symbol)

    def isWater(self, x,y):
        return list(self.gaGrid[x][y])[0] =='w'
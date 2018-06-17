import pandas as pd

class gaMap():
    def __init__(self):
        self.gaGrid = pd.read_csv('app_resources/map.csv', sep=',',header=None)

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
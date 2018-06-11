import pandas as pd


def init():
    global gaGrid
    gaGrid = pd.read_csv('app_resources/map.csv', sep=',',header=None)

def getCost(x,y):
    return int(list(gaGrid[x][y])[1])

def swicz(x):
    return {
        'w': 'water',
        'f': 'background_lines',
        'm': 'mountains',
        'b': 'bush',
        's': 'swamp',
    }.get(x, 9) 

def getFilename(x,y):
    symbol = list(gaGrid[x][y])[0]
    return swicz(symbol)

def isWater(x,y):
    return list(gaGrid[x][y])[0] =='w'
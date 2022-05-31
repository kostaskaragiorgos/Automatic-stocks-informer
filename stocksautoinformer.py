import os
from matplotlib import ticker

import yfinance
PORTFOLIO = ["GPS", "KO", "AAPL", "RWT", "AEO", "T" ]

def getlistoftickers(listofstocknames):
    yfobjects = []
    for stock in listofstocknames:
        yfobjects.append(yfinance.Ticker(stock))
    return yfobjects

def foldercreation(listofstocknames):
    """
    Creates a folder for each element of the list
    Args:
        listofstocknames: a list of stock names
    """
    for stock in listofstocknames:
        os.mkdir(stock)


foldercreation(PORTFOLIO)
tickers = getlistoftickers(PORTFOLIO)


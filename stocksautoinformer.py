import os
from matplotlib import ticker
import pandas as pd

import yfinance
PORTFOLIO = ["GPS", "KO", "AAPL", "RWT", "AEO", "T" ]

def getlistoftickers(listofstocknames):
    """saves Ticker objects to a list
    Args:
        listofstocknames: a list of stock names
    Returns:
        yfobjects: a list of Ticker objects
    """
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


def getdividends(tickernames,tickers):
    for i in range(len(tickers)):
        os.chdir(tickernames[i])
        df = tickers[i].dividends
        df.to_csv("dividends"+str(tickernames[i])+".csv")
        os.chdir("..")

foldercreation(PORTFOLIO)
tickers = getlistoftickers(PORTFOLIO)
getdividends(tickernames=PORTFOLIO, tickers=tickers)

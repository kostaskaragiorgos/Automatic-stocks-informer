import os
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
import csv


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
        if not os.path.exists(stock):
            os.mkdir(stock)


def getdividends(tickernames,tickers):
    """saves a dividends.csv file for each ticker.
    Args:
        tickernames: a list with the names of tickers
        tickers: a list with ticker objects

    """
    for i in range(len(tickers)):
        os.chdir(tickernames[i])
        df = tickers[i].dividends
        df.to_csv("dividends "+str(tickernames[i])+ str(date.today())+".csv")
        os.chdir("..")


def get_info(ticker, typeofinfo, allinfo=False):
    if allinfo:
        return ticker.info
    return ticker.info.get(str(typeofinfo))

def saveinfotocsv(tickernames, tickers, typeofinfo= "", allinfo=False):
    if allinfo:
        for i in range(len(tickers)):
            os.chdir(tickernames[i])
            df = pd.DataFrame.from_dict(tickers[i].info, orient='index')
            df.to_csv("info "+str(tickernames[i])+ str(date.today())+".csv")
            os.chdir("..")


foldercreation(PORTFOLIO)
tickers = getlistoftickers(PORTFOLIO)
getdividends(tickernames=PORTFOLIO, tickers=tickers)
saveinfotocsv(tickernames=PORTFOLIO, tickers=tickers, allinfo=True)

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

def get_info(ticker, typeofinfo, allinfo=False):
    if allinfo:
        return ticker.info
    return ticker.info.get(str(typeofinfo))

def saveinfotocsv(tickernames, tickers, typeofinfo= "", allinfo=False):
    for i in range(len(tickers)):
        os.chdir(tickernames[i])
        if allinfo:
            df = pd.DataFrame.from_dict(tickers[i].info, orient='index')
            df.to_csv("info "+str(tickernames[i])+ str(date.today())+".csv")
            
        else:
            for j in range(len(typeofinfo)):
                df = getattr(tickers[i], typeofinfo[j])
                df.to_csv(str(typeofinfo[j])+str(tickernames[i])+ str(date.today())+".csv")

        os.chdir("..")



def saveplot(tickernames, tickers,type, infotoplot):
    for i in range(len(tickers)):
        os.chdir(tickernames[i])
        for j in range(len(infotoplot)):
            df = getattr(tickers[i], infotoplot[j])
            df.plot(kind=type)
            plt.savefig(str(infotoplot[j])+" of " + str(tickernames[i])+".png")
        os.chdir("..")

numeric_indicators = ['quarterly_earnings', 'earnings']
musthaveinfo = ['recommendations','cashflow', 'balance_sheet', 'quarterly_balance_sheet', 'quarterly_cashflow','dividends', 'financials', 'quarterly_financials']

foldercreation(PORTFOLIO)
tickers = getlistoftickers(PORTFOLIO)
saveinfotocsv(tickernames=PORTFOLIO, tickers=tickers, allinfo=True)
saveplot(PORTFOLIO, tickers, "bar", numeric_indicators)
saveinfotocsv(tickernames= PORTFOLIO, tickers=tickers, typeofinfo= musthaveinfo, allinfo=False)

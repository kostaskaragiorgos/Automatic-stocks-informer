import yfinance as yf
class Portfolio():
    def __init__(self, name):
        self.name = name
        self.tickers = {}

    def setname(self, name):
        self.name = name
    
    def getname(self):
        return self.name
    
    def add_ticker(self, nameofthestock, tickerofthestock):
        self.tickers = {nameofthestock: yf.Ticker(tickerofthestock)}
    




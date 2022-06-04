import yfinance as yf
class Portfolio():
    def __init__(self, name):
        self.name = name
        self.tickers = {}
    def setname(self, name):
        self.name = name


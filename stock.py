
import yfinance as yf

class Stock():
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker
        self.stock = {name: yf.Ticker(ticker)}
    
    def getname(self):
        return self.name
    
    def getstock(self):
        return self.stock

    def get_yfobj(self):
        return self.stock.get(self.name)


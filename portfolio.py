
import yfinance as yf
from stock import Stock

class Portfolio():
    def __init__(self):
        self.name = "Test"
        self.stocks = []

    def setname(self, name):
        self.name = name
    
    def getname(self):
        return self.name

    def getstocks(self):
        return self.stocks
    
    def getname(self):
        return self.name

    def add_stock(self, stock):
        self.stocks.append(stock)

    def delete_stock(self, nameofthestock):
        for i in self.stocks:
            if nameofthestock == i.getname():
                self.stocks.remove(i)


    def print_portfolio(self):
        print("PORTFOLIO: " + self.getname() +"\n")
        for i in self.stocks:
            print(i.getname())


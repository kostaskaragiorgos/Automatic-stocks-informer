import yfinance as yf
class Portfolio():
    def __init__(self, name):
        self.name = name
        self.tickers = {}

    def setname(self, name):
        self.name = name
    
    def getname(self):
        return self.name
    
    def add_stock(self, nameofthestock, tickerofthestock):
        self.tickers = {nameofthestock: yf.Ticker(tickerofthestock)}
    
    def delete_stock(self, nameofthestock):
        self.tickers.pop(nameofthestock)
    
    def get_stock(self, nameofthestock):
        return self.tickers[nameofthestock]


    def show_portfolio(self):
        print("PORTFOLIO: " + self.getname() +"\n")
        for key, value in self.tickers.items():
            print(key, ':', value)


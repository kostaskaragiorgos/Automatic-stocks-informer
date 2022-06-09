
import sys
import pickle

 
from portfolio import Portfolio
from stock import Stock

 
 
 
class PortfolioCreator:
    def __init__(self):
        self.p = Portfolio()
        self.isloaded= False
        self.choices = {
    
            "1" : self.create_portfolio,

            "2" : self.load_portfolio,
    
            "3" : self.add_stock,
    
            "4" : self.delete_stock,

            "5" : self.show_portfolio,

            "6" : self.quit,
            }
    
    
    
    
    
    
    
    def display_menu(self):
    
        print(""" 
    
                Portfolio  Menu  
    
    
    
                1. Create Portfolio

                2. Load Portfolio
    
                3. Add stock
    
                4. Delete stock

                5. Show portfolio
    
                6. Quit program
    
                """)
    
    
    def run(self):
    
    
    
        while True:
    
            self.display_menu()
    
            choice = input("Enter an option: " )
    
            action = self.choices.get(choice)
    
            if action:
    
                    action()
    
            else:
    
                print("{0} is not a valid choice".format(choice))
    

    
    def create_portfolio(self):
        name = input("Enter the name of the portfolio" )
        self.p = Portfolio()
        self.p.setname(name)
    
    def add_stock(self):
        name = input("Enter the name of the stock")
        ticker = input("Enter the ticker of the stock")
        stock = Stock(name, ticker=ticker)
        self.p.add_stock(stock)


    
    def delete_stock(self):
        name = input("Enter the name of the stock")
        self.p.delete_stock(name)
    
    def show_portfolio(self):
        self.p.print_portfolio()
    
    def quit(self):
        file = open(self.p.getname(), 'wb')
        pickle.dump(self.p , file)
        sys.exit(0)
    
    def load_portfolio(self):
        name = input("Enter the name of the portfolio file")
        try:
            file = open(name, 'rb')
            self.p = pickle.load(file)
            file.close()
            self.isloaded = True
        except:
            print("There is no such portfolio")
    
    
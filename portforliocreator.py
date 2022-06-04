
import sys

 
from portfolio import Portfolio
 
 
 
class PortfolioCreator:

    def __init__(self):
        self.p = Portfolio()

    
        self.choices = {
    
            "1" : self.create_portfolio,
    
            "2" : self.add_stock,
    
            "3" : self.delete_stock,
    
            "4" : self.quit
    
            }
    
    
    
    
    
    
    
    def display_menu(self):
    
        print(""" 
    
                Portfolio  Menu  
    
    
    
                1. Create Portfolio
    
                2. Add stock
    
                3. Delete stock
    
                4. Quit program
    
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
    
        ''' Add a new diary in the diarybook '''
    
    
    
        name = input("Enter the name of the portfolio" )
        self.p.setname(name)
    
    def add_stock(self):
        name = input("Enter the name of the stock")
        ticker = input("Enter the ticker of the stock")
        self.p.add_stock(name, ticker)
    
    def delete_stock(self):
        name = input("Enter the name of the stock")
        self.p.delete_stock(name)
    
    def quit(self):
        sys.exit(0)
    
    
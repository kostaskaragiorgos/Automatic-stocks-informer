import pickle
import os
import pandas as pd
from datetime import date

def foldercreation(listofstocks):
    """
    Creates a folder for each element of the list
    Args:
        listofstocknames: a list of stock names
    """
    for stock in listofstocks:
        if not os.path.exists(stock.getname()):
            os.mkdir(stock.getname())
    


def saveinfotocsv(listofstocks, typeofinfo= "", allinfo=False):
    for stock in listofstocks:
        os.chdir(stock.getname())
        if allinfo:
            df = pd.DataFrame.from_dict(stock.get_yfobj().info, orient='index')
            df.to_csv("info "+str(stock.getname())+ str(date.today())+".csv")
        else:
            for j in typeofinfo:
                print(j)
                print(stock.getname())
                try:
                    df = getattr(stock.get_yfobj(), j)
                    print(df)
                    df.to_csv(str(j)+str(stock.getname())+ str(date.today())+".csv")
                except:
                    continue

        os.chdir("..")


try:
    file = open('kostas', 'rb')
    p = pickle.load(file)
    file.close()
except:
    print("There is no such file")


stocks = p.getstocks()
print(stocks)
foldercreation(stocks)
musthaveinfo = ['recommendations','cashflow', 'balance_sheet', 'quarterly_balance_sheet', 'quarterly_cashflow','dividends', 'financials', 'quarterly_financials']
saveinfotocsv(stocks, typeofinfo=musthaveinfo)
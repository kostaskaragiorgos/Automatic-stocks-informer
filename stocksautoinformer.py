import os

def foldercreation(listofstocknames):
    """
    Args:
        listofstocknames: a list of stock names
    """
    for stock in listofstocknames:
        os.mkdir(stock)
        os.chdir("..")


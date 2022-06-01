
from  stocksautoinformer import *
import pandas as pd
import yfinance

PORTFOLIO = ["GPS", "KO", "AAPL", "RWT", "AEO", "T" ]


def test_stocksautoinformer():
    assert len(PORTFOLIO) == len(getlistoftickers(PORTFOLIO))

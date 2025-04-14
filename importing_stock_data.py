import numpy as np
import typing
import yfinance as yf
import datetime as dt
import pandas as pd


def get_data(ticker: dict, start_date: str, end_date: str) -> None:
    """
    Uses yahoo finance module to pull data from Yahoo Finance.
    Each ticker is written into a csv file.


    Input: a dictionary of Ticker Symbols, start date and end date

    Format of CSV files: timestamp and close (to standardize with rest of the project)

    """

    for key, val in ticker.items():
        data = yf.Ticker(val)
        y = data.history(start=start_date, end=end_date)
        df = pd.DataFrame()
        df["timestamp"] = pd.to_datetime(y.index)
        df["timestamp"] = df["timestamp"].dt.date
        ## To keep things simple only copy the closing price.
        df["Close"] = y["Close"].to_numpy()
        file_name = key + ".csv"
        df.to_csv(file_name)


ticker_sym = {"vix": "^VIX", "spgsci": "GD=F"}
start_date = "2022-01-03"
end_date = "2025-03-14"
get_data(ticker_sym, start_date, end_date)

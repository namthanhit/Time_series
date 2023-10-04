import pandas as pd
import mplfinance as mpf

data = pd.read_csv("INTC.csv", index_col=0, parse_dates= True)
mpf.plot(data, type="line", style = "yahoo", title= "INTC",xlabel = "Date", ylabel = "Price", figsize=(12,6))

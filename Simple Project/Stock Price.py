# pip install yfinance


import yfinance as yf

STK = input("Enter share name: ").upper()

data yf.Ticker (STK).history (period="1d")

last_market_price = data['Close').iloc[-1]

print(f"Last market price {STK):", last_market_price)
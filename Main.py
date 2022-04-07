import requests
import matplotlib.pyplot as plt
import pandas as pd


s_price = []




#            ---DATA FORMAT---
#     1499040000000,      // Open time
#     "0.01634790",       // Open
#     "0.80000000",       // High
#     "0.01575800",       // Low
#     "0.01577100",       // Close
#     "148976.11427815",  // Volume
#     1499644799999,      // Close time
#     "2434.19055334",    // Quote asset volume
#     308,                // Number of trades
#     "1756.87402397",    // Taker buy base asset volume
#     "28.46694368",      // Taker buy quote asset volume
#     "17928899.62484339" // Ignore.

def download_new_data( crypto="ETH", currency="EUR"):
    stock_data = requests.get("https://api.binance.com/api/v1/klines?&symbol=ETHEUR&interval=3m").json()
    for i, element in enumerate(stock_data):
            print(element[1])
            s_price.append(element[1])

    c_df = pd.DataFrame(stock_data, columns=['date', 'open', 'high', 'low', 'close', 'Volume', 'Close time','Quote asset volume', 'Trades','Tbbav', 'Tbqav', 'ig'])
    c_df.set_index('date', inplace=True)
    print(c_df.head())
    c_df.to_csv('ETCEUR.csv')



position = [0, 100, 200, 300]

plt.plot(s_price, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')




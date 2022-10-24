import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime

def get_price(url, symbol, interval, limit):
    params = {
        'limit': limit,
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    res = requests.get(url = url, params = params)
    data = res.json()
    return data

URL_PRICE = 'https://api.binance.com/api/v3/klines'
symbol = 'DARUSDT'
invest = 2
price_data = get_price(URL_PRICE, symbol, '15m', 1000)

df = pd.DataFrame(columns=['time', 'open', 'close', 'high','low'])
# append with dic # df.append({'time':0,'open':1,'close':2,'high':3,'low':4},ignore_index=True)
# append with list # df.loc[len(df)] = [1, 2, 3, 4, 5]

for item in price_data:
    new_row = {}
    closetime = datetime.utcfromtimestamp(item[6]/1000).strftime('%Y-%m-%d %H:%M:%S') #+ timedelta(hours=7)
    open = float(item[1])
    close = float(item[4])
    high = float(item[2])
    low = float(item[3])
    new_row['time'] = closetime
    new_row['open'] = open
    new_row['close'] = close
    new_row['high'] = high
    new_row['low'] = low
    df = df.append(new_row, ignore_index=True)

# Bollinger Band Algorithm
period = 20
df['SMA'] = df['close'].rolling(window=period).mean()
df['STD'] = df['close'].rolling(window=period).std()
df['upper'] = df['SMA'] + 2*df['STD']
df['lower'] = df['SMA'] - 2*df['STD']
df['buy_signal'] = np.where(df.lower > df.close, True, False)
df['sell_signal'] = np.where(df.upper < df.close, True, False)
df.dropna()
plot_col = ['time','close', 'SMA', 'upper', 'lower']

# Picking sell/buy signal
buy = []
sell = []
buy_quantity = []
invest_change = [invest]
already_bought = False

for i in range(len(df)):
    if df.lower[i] > df.close[i]:
        if already_bought == False:
            buy.append(i)
            buy_quantity.append(invest/df.close[i])
            already_bought = True
    elif df.upper[i] < df.close[i]:
        if already_bought == True and df.at[i,'close'] > df.at[buy[-1],'close']:
            sell.append(i)
            invest = buy_quantity[-1]*df.close[i]
            invest_change.append(invest)
            already_bought = False

print(buy)
print(sell)
print(buy_quantity)
print(invest_change)

# calculating profit
totalprofit = invest_change[-1] - invest_change[0]
percentprofit = totalprofit / invest_change[0]
print(totalprofit)
print(percentprofit)

# Plotting result
df[plot_col].plot(figsize = (12.2, 6.4), x ='time')
plt.title('Bollinger Band {}'.format(symbol))
plt.ylabel('Price in USDT')
plt.fill_between(df.time, df.upper, df.lower, color = 'grey', alpha = 0.5)
# plt.scatter(df.time[df.buy_signal], df[df.buy_signal].close, marker = '^', color='g')
# plt.scatter(df.time[df.sell_signal], df[df.sell_signal].close, marker = 'v', color='r')
plt.scatter(df.iloc[buy].index, df.iloc[buy].close, marker = '^', color='g')
plt.scatter(df.iloc[sell].index, df.iloc[sell].close, marker = 'v', color='r')
plt.plot(df.iloc[[buy[0]]].index, invest_change[0], marker = 'o', color='r')
plt.scatter(df.iloc[sell].index, invest_change[1:], marker = 'o', color='black')

plt.show()

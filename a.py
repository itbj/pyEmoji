import pandas_datareader as web
#import pandas as pd
#import datetime as dt
import math
#pip install colorama
import colorama


def progress_bar(progress, total,color=colorama.Fore.YELLOW):
    percent = 100 * ( progress / float(total))
    bar = '█' * int (percent) + '-'*(100- int(percent))
    print (color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print (colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")

tickers=["AAPL","FB","TSLA","NVDA","GS","WFC"]  # AAPL not APPL 
closing_prices=[]


progress_bar(0,len(tickers))
for index, ticker in enumerate(tickers):
    #last_price = web.DataReader(ticker, "yahoo",start='2022-09-16', end='2022-09-16').iloc[-1]['Close']
    last_price = web.DataReader(ticker, "yahoo").iloc[-1]['Close']
    closing_prices.append(last_price)
    progress_bar(index +1,len(tickers))


#print (closing_prices)
#https://youtu.be/x1eaT88vJUA?t=488
#error key word date?
#https://pandas-datareader.readthedocs.io/en/latest/
#https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-yahoo
print (colorama.Fore.RESET)

# numbers = [x *5 for x in range(2000,3000)]
# results=[]

# print (numbers)
# progress_bar(0,len(tickers))
# for i, x in enumerate(numbers):
#     results.append(math.factorial(x))   # 阶乘
#     results.append(math.sqrt(x))        # sqrt
#     progress_bar(i+1,len(numbers))
# print (colorama.Fore.RESET)
#print (results)   # errors?? ValueError: Exceeds the limit (4300) for integer string conversion


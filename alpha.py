import requests
from datetime import date, timedelta
from stocksList import StocksList
from search import Search

key = 'MRICNP7VE0JIA7QB'

class AlphaVantage():
    def closing_price(timeframe):
        while True:
            print('Which NYSE ticker do you want to look at? ')
            stock_ticker = input('Alternatively use L to list or Q to return to the main menu: ').upper()
            result = Search.binary_search(StocksList.NYSE_list(), stock_ticker)
            if result != -1:
                break
            else:
                if stock_ticker == "L":
                    print(StocksList.NYSE_list())
                elif stock_ticker == "Q":
                    return
        if timeframe == "yesterday":
            AlphaVantage.api_call_close(stock_ticker)
        else:
            AlphaVantage.api_call_month(stock_ticker)

    def api_call_close(stock):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&apikey={1}'.format(stock, key)
        r = requests.get(url)
        data = r.json()

        yesterday_date = str(date.today() - timedelta(days=1))
        yesterday_data = data["Time Series (Daily)"][yesterday_date].get('4. close')

        print("\nYesterdays closing price for {0}: ${1}".format(stock,yesterday_data[:-2]))

    def api_call_month(stock):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&apikey={1}'.format(stock, key)
        r = requests.get(url)
        data = r.json()

        previous_month = []
        for i in range(1, 30):
            try:
                yesterday_data = data["Time Series (Daily)"][str(date.today() - timedelta(days=i))].get('4. close')[:-2]
                previous_month.append("{} - ".format(stock) + str(date.today() - timedelta(days=i)))
                previous_month.append(' - $' + str(yesterday_data))
                previous_month.append('\n')
            except KeyError:
                continue
        previous_month = ''.join(previous_month)
        print(previous_month)
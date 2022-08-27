class StocksList():
    def NYSE_list():
        with open(r"stockTickers\NYSE_stocks.txt") as file:
            str = file.read()
            stock_list = str.split(',')
        return stock_list
    def Nasdaq_list():
        with open(r"stockTickers\Nasdaq_stocks.txt") as file:
                str = file.read()
                stock_list = str.split(',')
        return stock_list
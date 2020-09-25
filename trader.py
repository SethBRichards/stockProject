import stockToolbox as stb
import singleStockBuy as ssb

class trader:

    # contains all stocks owned by trader
    portfolio = {}

    # initializes trader name and amount of money to invest
    def __init__(self, trader_name, money):
        self.trader_name = trader_name
        self.money = money

    # buys specified amount of stock in given stock name
    def buy(self, stockname, amount):
        stockname = stockname.upper()

        # gets current price per share from Yahoo finance
        current_stock_price = stb.stockPriceGrab(stockname)

        # converts dollars to shares if necessary
        amount = stb.amount2shares(stockname, amount, current_stock_price)

        # checks if trader can afford trade
        if self.money - current_stock_price * amount < 0:
            return False

        self.money = self.money - current_stock_price * amount
        if stockname in self.portfolio:
            self.portfolio[stockname].add(amount)
            return True
        else:
            self.portfolio[stockname] = ssb.singleStockBuy(stockname, amount, current_stock_price)
            return True


    # def sell(self, stockname):
    #     print('You have ' + self.portfolio[stockname].shares + '(' + ') of ' + stockname + '.')
    #

    # sells specified shares of stock by amount
    def sell(self, stockname, amount):
        if stockname in self.portfolio:
            amount = stb.amount2shares(stockname, amount)
            if self.portfolio[stockname].shares - amount > 0:
                self.portfolio[stockname].add(-1 * amount)
                return True
        return False

    def value(self):
        total = 0.0
        for key in self.portfolio:
            total = total + self.portfolio[key].value()
        return total


x = trader('joe',15)
x.buy('TSLA', '$10')
x.buy('TSLA', '$10')
#x.sell('TSLA', '$10')

print(x.value())
print(x.money)
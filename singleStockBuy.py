import stockToolbox as stb

# Contains original purchase price and name of stock
class singleStockBuy:

    def __init__(self, stockname, shares, purchaseprice):
        self.stockname = stockname
        self.shares = shares
        self.purchaseprice = purchaseprice
        self.ptime,self.pdate = stb.currenttime()

    def value(self):
        return self.shares * stb.stockPriceGrab(self.stockname)

    def add(self, amount):
        self.shares = self.shares + amount

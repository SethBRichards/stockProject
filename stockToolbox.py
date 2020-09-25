from lxml import html
import requests
from datetime import datetime
from datetime import date

#stockToolbox contains several helper functions related to gathering, storing, and processing trading data

# stockPriceGrab scrapes the Yahoo finance website for live  price of specified stock
def stockPriceGrab(stockname):

    website = 'https://finance.yahoo.com/quote/' + stockname + '/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACZbH-lQ5uoS9YgEHu8OxF3FjMOBhy2ocQK4NCrd_habF1kn-6s1jH51EuwaVnyDgMq4AK3merUN5UD7BCGEdnBJdrdpeJgsHz56S-K81cq0m0nQlqigGCNcN5RTtgER4BSamu2Qg3-zFPI8RT_7U4pDAe1wmq-NyKUn39zR7IVc'
    page = requests.get(website)
    tree = html.fromstring(page.content)

    live_price = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()')

    return float(live_price[0])

#returns the current time and date
def currenttime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time = current_time
    today = date.today()

    return time, today

# returns number of shares of stock if given, calculates number of shares if dollars given
def amount2shares(stockname, amount, currentPrice = 0):
    if isinstance(amount, str):
        if currentPrice == 0:
            currentPrice = stockPriceGrab(stockname)
        amount = amount.partition("$")[2]
        amount = float(amount) / currentPrice
    return amount

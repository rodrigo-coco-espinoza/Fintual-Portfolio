#Construct a simple Portfolio class that has a collection of Stocks and a “Profit” method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a “Price” method that receives a date and returns its price. 

import datetime
import yfinance as yf

def check_stock_exists(stock):
    """
    Comprueba si el stock existe en el mercado.
    """

    stock_data = yf.Ticker(stock.upper())
    if stock_data.history(period="1d").empty:
        return False
    else:
        return True

def check_date(date):
    """
    Comprueba si la fecha introducida es válida.
    """

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False

class Stock:
    def __init__(self, name):

        if not check_stock_exists(name):
            raise ValueError("Stock no existe en el mercado.")

        self.name = name.upper()


    def getPrice(self, date):
        """
        Devuelve el precio del stock en la fecha dada.
        La fecha debe tener el formato "YYYY-MM-DD".
        """

        if not check_date(date):
            raise ValueError("Fecha inválida. El formato debe ser 'YYYY-MM-DD'.")

        stock_data = yf.Ticker(self.name)
        price = stock_data.history(start=date).iloc[0]["Close"]
        
        return price


class Portfolio:

    def __init__(self):
        self.stocks = []

    def addStock(self, stock):
        """
        Añade un stock al portfolio.
        stock debe ser un objeto de la clase Stock.
        """

        if not isinstance(stock, Stock):
            raise ValueError("stock debe ser un objeto de la clase Stock.")
        
        self.stocks.append(stock)
    
    def profit(self, date1, date2):
        """ 
        Devuelve el beneficio del portfolio entre dos fechas.
        date1 y date2 deben tener el formato "YYYY-MM-DD".
        """

        if not check_date(date1) or not check_date(date2):
            raise ValueError("Fecha inválida. El formato debe ser 'YYYY-MM-DD'.")

        profit = 0
        for stock in self.stocks:
            price1 = stock.getPrice(date1)
            price2 = stock.getPrice(date2)
            profit += price2 - price1


while True:

    stock = input("Introduce el nombre del stock: ")
    stock = Stock(stock)
    date = input("Introduce la fecha (YYYY-MM-DD): ")
    stock.getPrice(date)

    input("Presiona Enter para continuar...")


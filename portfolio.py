from datetime import datetime
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
        datetime.strptime(date, "%Y-%m-%d")
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
    
    def getProfit(self, start_date, end_date):
        """ 
        Devuelve el beneficio del portfolio entre dos fechas.
        start_date y end_date deben tener el formato "YYYY-MM-DD".
        """

        if not check_date(start_date) or not check_date(end_date):
            raise ValueError("Fecha inválida. El formato debe ser 'YYYY-MM-DD'.")
        
        profit = 0
        for stock in self.stocks:
            start_price = stock.getPrice(start_date)
            end_price = stock.getPrice(end_date)
            profit += end_price - start_price
        
        return profit
    

    def getAnnualizedReturn(self, start_date, end_date):
        """
        Devuelve el retorno anualizado del portfolio entre dos fechas.
        start_date y end_date deben tener el formato "YYYY-MM-DD".
        """

        if not check_date(start_date) or not check_date(end_date):
            raise ValueError("Fecha inválida. El formato debe ser 'YYYY-MM-DD'.")
        

        profit = 0
        for stock in self.stocks:
            start_price = stock.getPrice(start_date)
            end_price = stock.getPrice(end_date)
            days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
            annualized_return = (end_price / start_price) ** (365 / days) - 1
            profit += annualized_return

        return profit

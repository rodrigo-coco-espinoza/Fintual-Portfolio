# Stocks Portfolio
Implementación en Python para gestionar un portafolio de acciones. Permite verificar la existencia de acciones, recuperar precios históricos y calcular tanto el beneficio como el retorno anualizado en períodos específicos.

## Características
**Clase Stock**: Representa una acción individual, permitiendo obtener su valor en fechas específicas.  
**Clase Portfolio**: Gestiona una colección de acciones, permitiendo calcular los beneficios y el retorno anualizado entre dos fechas.  
**Validación de fechas y stocks**: Incluye validaciones para asegurar que la acción existe en el mercado y que las fechas tienen el formato correcto.

## Requisitos
Python 3.x  
Biblioteca yfinance: Para obtener datos de acciones.

Instalar mediante pip:
`pip install yfinance`

## Uso

### Clase Stock
**Inicialización**: Crea una instancia de Stock pasando el símbolo de la acción (por ejemplo, "AAPL" para Apple Inc.).

```
from stock_portfolio import Stock

apple = Stock("AAPL")
```

**getPrice**: Obtiene el precio de la acción en una fecha específica.

```
price = apple.getPrice("2023-01-01")
print(f"Precio el 2023-01-01: ${price}")
```

### Clase Portfolio
**Inicialización**: Crea una instancia de Portfolio.

```
from stock_portfolio import Portfolio

mi_portafolio = Portfolio()
```

**addStock**: Añade un objeto Stock al portafolio.

```
mi_portafolio.addStock(apple)
```

**getProfit**: Calcula el beneficio del portafolio entre dos fechas.

```
profit = mi_portafolio.getProfit("2023-01-01", "2024-01-01")
print(f"Profit: ${profit}")
```
**getAnnualizedReturn**: Calcula el retorno anualizado del portafolio entre dos fechas.

```
annualized_return = mi_portafolio.getAnnualizedReturn("2023-01-01", "2024-01-01")
print(f"Retorno Anualizado: {annualized_return * 100:.2f}%")
```

## Ejemplo
```
from stock_portfolio import Stock, Portfolio

# Crear instancias de acciones
apple = Stock("AAPL")
microsoft = Stock("MSFT")

# Crear un portafolio y añadir acciones
mi_portafolio = Portfolio()
mi_portafolio.addStock(apple)
mi_portafolio.addStock(microsoft)

# Calcular el beneficio y el retorno anualizado
profit = mi_portafolio.getProfit("2023-01-01", "2024-01-01")
annualized_return = mi_portafolio.getAnnualizedReturn("2023-01-01", "2024-01-01")

print(f"Beneficio Total: ${profit}")
print(f"Retorno Anualizado: {annualized_return * 100:.2f}%")
```
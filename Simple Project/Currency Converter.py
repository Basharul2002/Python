# pip install currencyconverter


from currency_converter import Currency Converter

def convert currency (amount, from_currency, to_currency):
     c = CurrencyConverter()
     return c.convert(amount, from_currency, to_currency)


# Taking user inputs
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()


# Performing the conversion
converted_amount =  convert_currency (amount, from_currency, to_currency)


# Displaying the result
print("(amount) (from_currency) is equal to (converted_amount:.2f) (to_currency}")
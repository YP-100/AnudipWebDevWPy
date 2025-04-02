#question 1

class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):         #__add__ to override what + do
        if not isinstance(other, CustomString):
            raise TypeError("Can only concatenate CustomString with another CustomString")
        return CustomString(self.value + other.value)
    def __mul__(self, times):         #__mul__ to override what * do
        if not isinstance(times, int):
            raise TypeError("Can only multiply CustomString by an integer")
        if times < 0:
            raise ValueError("Cannot multiply CustomString by a negative number")
        return CustomString(self.value * times)

    def to_upper(self):              #just converts to uppercase
        return self.value.upper()

    def __str__(self):
        return self.value

s1 = CustomString("Hello")
s2 = CustomString("World")
s3 = s1 + s2
print(s3)
print(s1 * 3)
print(s1.to_upper())

#question 2

class Currency:
    exchange_rates = {           # exchange rates example will be used to convert currencies
        ("USD", "INR"): 86.32,   # 1 USD = 86.32 INR
        ("INR", "USD"): 1/86.32,
        ("EUR", "USD"): 1.09,    #1 EUR = 1.09 USD
        ("USD", "EUR"): 1/1.09,
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency == other.currency:
            return Currency(self.amount + other.amount, self.currency)
        raise ValueError("Cannot add amounts in different currencies")

    def convert_to(self, target_currency):
        if self.currency == target_currency:
            return Currency(self.amount, self.currency)
        key = (self.currency, target_currency)
        if key in self.exchange_rates: 
            # will match in exchange_rates dictionary
            converted_amount = self.amount * self.exchange_rates[key]
            return Currency(converted_amount, target_currency)
        raise ValueError("Exchange rate not available")

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

money1 = Currency(51, "USD")
money2 = Currency(35, "USD")

total_money = money1 + money2

converted_INR = money1.convert_to("INR")
converted_EUROS = money1.convert_to("EUR")

print(total_money)
print(converted_INR)
print(converted_EUROS)


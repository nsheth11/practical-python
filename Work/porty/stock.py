from tokenize import String
from . import typedproperty

class Stock:
    '''
    Represents a stock holding with name,shares and price attributes
    '''

    name = typedproperty.String('name')
    shares = typedproperty.Int('shares')
    price = typedproperty.Float('price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f'Stock(\'{self.name}\',{self.shares:d},{self.price:.2f})'

    def __str__(self) -> str:
        return f'({self.name},{self.shares:d},{self.price:.2f})'


    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, noofshares):
        self.shares -= noofshares

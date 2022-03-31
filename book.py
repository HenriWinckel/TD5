class Book:
    def __init__(self, name):
        self.name = name
        self.buy_list = []
        self.sell_list = []
    
    def insert_buy(self, qty, price):
        self.buy_list.append([qty, price])

    def insert_sell(self, qty, price):
        self.sell_list.append([qty, price])
    

class Order:
    def __init__(self):
        return
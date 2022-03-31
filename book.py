class Book:
    def __init__(self, name):
        self.name = name
        self.buy_list = []
        self.sell_list = []
        self.count = 0
    
    def insert_buy(self, qty, price):
        self.buy_list.append(Order(qty, price, "buy", self.count+1))
        self.count += 1

        print(f"--- Insert BUY {qty}@{price} id={self.count} on {self.name}")

    def insert_sell(self, qty, price):
        self.sell_list.append(Order(qty, price, "sell", self.count+1))
        self.count += 1
        print(f"--- Insert SELL {qty}@{price} id={self.count} on {self.name}")


class Order:
    def __init__(self, qty, price, type, id):
        self.qty = qty
        self.price = price
        self.type = type
        self.id = id
        return
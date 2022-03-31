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

        self.execute()
        self.status()



    def insert_sell(self, qty, price):
        self.sell_list.append(Order(qty, price, "sell", self.count+1))
        self.count += 1

        print(f"--- Insert SELL {qty}@{price} id={self.count} on {self.name}")

        self.execute()
        self.status()

    def status(self):
        print(f"Book on {self.name}")

        if len(self.sell_list) > 0:
            for sell in self.sell_list:
                print(sell)

        if len(self.buy_list) > 0:
            for buy in self.buy_list:
                print(buy)



    def execute(self):
        for sell in self.sell_list:
            for buy in self.buy_list:
                if sell.price == buy.price:
                    if sell.qty > buy.qty:
                        print(f"Execute {buy.qty} at {buy.price} on {self.name}")
                        sell.qty -= buy.qty
                        self.buy_list.remove(buy)
                    elif sell.qty < buy.qty:
                        print(f"Execute {sell.qty} at {sell.price} on {self.name}")
                        buy.qty -= sell.qty
                        self.sell_list.remove(sell)
                        break
                    else:
                        print(f"Execute {sell.qty} at {sell.price} on {self.name}")
                        break

class Order:
    def __init__(self, qty, price, type, id):
        self.qty = qty
        self.price = price
        self.type = type
        self.id = id
    
    def __str__(self):
        return f"\t{self.type.upper()} {self.qty}@{self.price} id={self.id}"
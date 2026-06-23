class product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def get_info(self):
        print(f"price of {self.name} is {self.price}")

p1= product("phone", 10_000)
p2=product("laptop", 50_000)

p1.get_info()

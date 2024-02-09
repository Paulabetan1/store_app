class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def view(self):
        return f'--------------------\nname: {self.name} \nprice: {self.price} \nstock: {self.stock}\n'



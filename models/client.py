from models.person import Person


class Client(Person):

    def __init__(self, document, name, lastname, age, total_purchases, total_discount):
        super().__init__(name, lastname, age)
        self.document = document
        self.total_purchases = total_purchases
        self.total_discount = total_discount

    def view(self):
        return f'--------------------\n' \
               f'document: {self.document} \n' \
               f'total_purchases: {self.total_purchases} \n' \
               f'total_discount: {self.total_discount}\n'

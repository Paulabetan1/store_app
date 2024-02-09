from models.person import Person


class Distributor(Person):

    def __init__(self, enterprise, debt, pbx, name, lastname, age):
        super().__init__(name, lastname, age)
        self.enterprise = enterprise
        self.debt = debt
        self.pbx = pbx

    def view(self):
        print(f'enterprise: {self.enterprise} \ndebt: {self.debt} \npbx: {self.pbx}')

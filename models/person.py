class Person:

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def show(self):
        print(f'name: {self.name} \nlastname: {self.lastname} \nage: {self.age}')

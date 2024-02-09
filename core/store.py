from utils import utils
from models.client import Client
from models.distributor import Distributor
from models.product import Product


class Store:
    name = 'Mascotas para todos'
    product_list = []
    client_list = []
    distributor_list = []

    def create(self, latest):
        self.product_list.append(Product('Arena', 15000, 10))
        self.product_list.append(Product('Max Cat', 144000, 5))
        self.product_list.append(Product('Collar de gato', 5000, 9))
        self.product_list.append(Product('Dog show', 4000, 30))

        self.client_list.append(Client(1, 'Pepito', 'Perez', 23, 0, 0))
        self.client_list.append(Client(1, 'Olga', 'Zan', 23, 0, 0))
        self.client_list.append(Client(1, 'Tuma', 'Má', 23, 0, 0))
        self.client_list.append(Client(1, 'PvP o miedo', ':v', 23, 0, 0))

        self.distributor_list.append(Distributor('Purina', 0, 12345, 'Marcos', 'Toro', 38))
        self.distributor_list.append(Distributor('Mascotas la 70', 0, 12345, 'Carlitos', 'XD', 38))
        self.distributor_list.append(Distributor('Exito', 0, 12345, 'Juan', 'Casas', 38))
        self.distributor_list.append(Distributor('Euro', 0, 12345, 'Benito', 'Camelo', 38))

        if not latest:
            self.show_menu()

    def show_menu(self):
        while True:
            print(f'************************ \n{self.name.upper()} \n************************')

            option = utils.validate_number('Seleccione una opción: \n'
                                           '1. Mostrar todos los productos. \n'
                                           '2. Agregar un producto. \n'
                                           '3. Eliminar un producto. \n'
                                           '4. Mostrar todos los clientes. \n'
                                           '5. Mostrar todos los distribuidores. \n'
                                           '0. Salir.\n')

            match option:
                case 0:
                    break
                case 1:
                    utils.show_list(self.product_list, 'productos')
                case 2:
                    self.add_product()
                case 3:
                    self.delete_product()
                case 4:
                    utils.show_list(self.client_list, 'clientes')
                case 5:
                    utils.show_list(self.distributor_list, 'distribuidores')
                case _:
                    print('Opción no encontrada')

    def add_product(self):
        print('Ingrese el nuevo producto')

        name = input('Ingrese el nombre: ')
        price = utils.validate_number('Ingrese el precio: ')
        stock = utils.validate_number('Ingrese la cantidad: ')

        new_product = Product(name, price, stock)

        self.product_list.append(new_product)

        print('El producto se ha ingresado correctamente')
        new_product.view()

    def delete_product(self):
        product_to_delete = input('Ingrese el nombre del producto a eliminar: ')
        product_found = False
        index = 0

        for i, product in enumerate(self.product_list):
            if product.name.upper() == product_to_delete.upper():
                product_found = True
                index = i
                break

        if product_found:
            self.validate_delete(self.product_list[index], index)
        else:
            print('El producto no se encuentra registrado')

    def validate_delete(self, product, index):

        stock_to_delete = utils.validate_number(f'Ingrese a cantidad a eliminar, hay {product.stock} unidades: ')

        if stock_to_delete > product.stock:
            print(f'No hay suficiente cantidad para eliminar, unidades disponible: {product.stock}')
        elif stock_to_delete == product.stock:
            del self.product_list[index]
            print('Se eliminaron todas las unidades, ya no existe el producto.')
        else:
            product.stock = product.stock - stock_to_delete
            print(f'Las unidades se han eliminado exitosamente, quedan {product.stock}')

"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.__name

    def make_sound(self):
        self.make_sound()

class Lion(Animal):
    def __init__(self):
        super().__init__(name)
        self.som = 'roar'

    def make_sound():
        print(self.som)

class Mouse(Animal):
    def __init__(self):
        super().__init__(name)
        self.som = 'squek'

    def make_sound():
        print(self.som)

animals = [
    Lion('lion'),
    Mouse('mouse')
]


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Discount(Cliente):
    def __init__(self,price):
        super().__init__(customer, desconto)
        self.price = price

    def give_discount(self):
            return self.price * self.desconto


class Cliente:
    def __init__(self, customer, desconto):
        self.customer = customer
        self.desconto = desconto


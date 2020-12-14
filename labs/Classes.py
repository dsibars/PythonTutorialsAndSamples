# CLAAASE
class Category(object):
    def __init__(self, name, difficulty):
        self.name = name
        self.dificulty = difficulty

# OBJEEETOS
categoria_reina = Category('motogp', 100)
categoria_mitja = Category('moto2', 60)
categoria_inicial = Category('moto3', 30)

# CLAAASE
class Driver(object):
    def __init__(self, name, age, category):
        self.name = name
        self.age = age
        self.category = category

# OBJEEETOS
dovizioso = Driver('Andrea dovizioso', 34, categoria_reina)
alex_m = Driver('Alex márquez', 25, categoria_reina)
arenas = Driver('Albert arenas', 20, categoria_mitja)

# CLAAASE
class Presentador(object):
    def __init__(self, name):
        self.name = name

    def introdueix_pilot(self, driver):
        message = 'buenos dias, soy ' + self.name + ' y os presento a ' + driver.name + ' de la categoria ' + driver.category.name
        print(message)

# OBJEEETO
ernest = Presentador('ernest rivera')


# UNA VEZ LO PREPARAMOS, SE USA
ernest.introdueix_pilot(alex_m)


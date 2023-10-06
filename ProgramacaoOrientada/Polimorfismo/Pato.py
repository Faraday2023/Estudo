from Animal import *

class Pato(Animal):
    def __init__(self):
        Animal.__init__(self)

    def emitir_som(self):
        print('Quack.')
        
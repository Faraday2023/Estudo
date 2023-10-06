from Animal import *

class Homem(Animal):
    def __init__(self):
        Animal.__init__(self)
        pass

    def emitir_som(self):
        print('Homem falando.')

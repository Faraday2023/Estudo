from Animal import *

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)

    def emitir_som(self):
        print('Au au.')
        
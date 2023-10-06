from FiguraGeométrica import *

class Circulo(FiguraGeométrica):
    from math import pow
    def __init__(self, raio):
        FiguraGeométrica.__init__(self,nome=str)
        self.raio = raio

    def calcula_área(self):
        área = 3.14*pow(self.raio,2)
        return área
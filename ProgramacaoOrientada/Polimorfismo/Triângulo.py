from FiguraGeométrica import *

class Triângulo(FiguraGeométrica):
    def __init__(self,base, altura):
        FiguraGeométrica.__init__(self,nome=str)
        self.base = base
        self.altura = altura

    def calcula_área(self):
        área = (self.base*self.altura)/2
        return área
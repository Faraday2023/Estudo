from FiguraGeométrica import *

class Quadrado(FiguraGeométrica):
    def __init__(self, lado):
        FiguraGeométrica.__init__(self,nome = str)
        self.lado = lado

    def calcula_área(self):
        área = self.lado**2
        return área
    
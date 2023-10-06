"""Uma associação permite duas classe se relacionarem, porém, são independentes, ou seja, não precisam uma da 
outra para existirem"""

class Escritor:
    def __init__(self,nome):
        self.__nome = nome # atributo privado, ou seja, não pode ser acessado fora da classe
        self.__ferramenta = None
    
    @property # com o getter podemos acessá-lo fora da classe
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self,marca):
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta escrevendo')

class MáquinaDeEscrever:

    def escrever(self):
        print('Máquina escrevendo')
    pass

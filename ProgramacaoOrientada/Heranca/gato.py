from pet import*

class Gato(Pet):
    def __init__(self,nome=str, idade=int, raça=str):
        Pet.__init__(self,nome, idade, raça)
    
    def miar(self):
        print('Miando')
        
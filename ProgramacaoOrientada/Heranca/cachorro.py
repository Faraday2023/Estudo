from pet import*

class Cachorro(Pet):
    def __init__(self,nome=str, idade=int, raça=str):
        Pet.__init__(self,nome, idade, raça)
    
    def latir(self):
        print('Latindo')
        
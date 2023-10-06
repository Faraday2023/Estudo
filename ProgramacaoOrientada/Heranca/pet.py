class Pet:
    def __init__(self,nome=str, idade=int, raça=str):
        self.nome  = nome
        self.idade = idade
        self.raça  = raça
    
    def brincar(self):
        print('Brincando')
        
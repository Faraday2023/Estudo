# getter and setters são proteções para o programa na hora de instanciar um objeto

class Produto:
    def __init__(self, nome,preço):
        self.nome = nome
        self.preço = preço
    
    def desconto(self, percentual):
        self.preço = self.preço - (self.preço*(percentual/100))
    
    @property #getter - recebe o preço
    def preço(self):
        return self._preço
    
    @preço.setter #setter - atualiza o preço
    def preço(self,valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', '')) #regex aqui ficaria melhor
        self._preço = valor
    
    @property #getter - recebe o nome
    def nome(self):
        return self._nome
    
    @nome.setter #setter - atualiza o nome
    def nome(self,valor):
        self._nome = valor.title()
    
p1 = Produto('Camiseta',50)
p1.desconto(10)
print(p1.nome)

p2 = Produto('Caneca',15)
p2.desconto(10)
print(p2.nome)

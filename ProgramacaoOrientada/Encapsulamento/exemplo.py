"""Encapsulamento serve para esconder certas partes do código, com o intuito de proteger alguma coisa
(classe, atributo, método)"""

"""
public = métodos e atributos acessados dentro e fora da classe
protect = métodos e atributos acessados dentro da classe pai e filha
private = métodos e atributos acessados naquela classe específica
_ = protect - significa que não deve ser acessado, ou seja, indica que a variável está protegida, porém, ainda é 
possível acessá-lo

__ = privado - significa que não deve ser acessado de maneira alguma, o python neste momento acessa um recurso e
 renomeia o atributo internamente. Só podendo ser acessado se "bd._BaseDeDados__dados".O comando  "bd.__dados" não
acessa a classe

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_clientes(self,id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2,'Miranda')
bd.inserir_cliente(3,'Rose')
print(bd.__dados)
bd.apaga_clientes(2)
bd.lista_clientes()

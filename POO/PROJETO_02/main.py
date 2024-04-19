# DISCIPLINA: PROGRAMAÇÃO ORIENTADA A OBJETO
# DESENVOLVEDOR: MARCOS PAULO P. CARNEIRO
# TURMA: 10° ENGEL

from abc import ABCMeta

class Endereço():
    def __init__(self, rua, numero, bairro,  cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def mostra_endereco(self):
        print(f'Rua: {self.rua} - Numero: {self.numero} - Bairro: {self.bairro} - Cidade: {self.cidade} - Estado: {self.estado} - CEP: {self.cep}')
    
class Pessoa(metaclass=ABCMeta):
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def apresentar(self):
        print(f'Meu nome é: {self.nome}')

class Servidor(Pessoa, metaclass=ABCMeta):
    def __init__(self, nome, cpf, endereco, siape):
        super().__init__(nome, cpf, endereco)
        self.siape = siape
    
    def apresentar(self):
        print(f'Meu nome é: {self.nome} - CPF: {self.cpf} - SIAPE: {self.siape}')

class Aluno(Pessoa):
    def __init__(self, nome, cpf, rua, numero, bairro, cidade, estado, cep, matricula, notas):   
        endereco = Endereço(rua, numero, bairro, cidade, estado, cep)
        super().__init__(nome, cpf, endereco)
        self.matricula = matricula
        self.notas = notas
        
    def calcula_cr_do_aluno(self):
        media = sum(self.notas)/(len(self.notas))
        print(f'O cr do aluno este semestre foi: {media}')
        
class Professor(Servidor):
    def __init__(self, nome, cpf, rua, numero, bairro, cidade, estado, cep, regime_de_trabalho, disciplinas, siape):
        
        endereco = Endereço(rua, numero, bairro, cidade, estado, cep)
        super().__init__(nome, cpf, endereco, siape)
        self.regime_de_trabalho = regime_de_trabalho
        self.disciplinas = disciplinas
    
    def disciplinas_lecionadas(self):
        print(f'As disciplinas lecionadas pelo professor {self.nome} esse semestre foram: {self.disciplinas}')

class Administrativo(Servidor):
    def __init__(self, nome, cpf, rua, numero, bairro, cidade, estado, cep, funcao, siape):
        endereco = Endereço(rua, numero, bairro, cidade, estado, cep)
        super().__init__(nome, cpf, endereco, siape)
        self.funcao = funcao

# MAIN

# OBJETOS
professor = Professor('Thomaz', 123456, 'Rua São Mateus', 187, 'Sernamby', 'São Mateus', 'ES', 29900, 44 , ['POO', 'TELECOM'], 123)
aluno = Aluno('Marcos', 123456, 'Rua Bosque', 50, 'Morada do Ribeirão', 'São Mateus', 'ES', 29900, 201001212, [10,9])

print('*'*100)
aluno.calcula_cr_do_aluno()
print('*'*100)
aluno.apresentar()
print('*'*100)
professor.apresentar()
print('*'*100)
professor.disciplinas_lecionadas()
print('*'*100)
professor.endereco.mostra_endereco()
print('*'*100)

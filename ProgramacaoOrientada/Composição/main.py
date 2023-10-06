from exemplo import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereço('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_endereços()
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereço('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_endereços()
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereço('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_endereços()
print()
from exemplo import Escritor
from exemplo import Caneta
from exemplo import MáquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
máquina = MáquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
máquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

class Motocicleta:
    def __init__(self, aro, marca, qtde_raios_roda): # Parâmetros da classe

        self.aro             = aro # 1° Argumento
        self.marca           = marca # 2° Argumento
        self.qtde_raios_roda = qtde_raios_roda # 3° Argumento
    
    def acelerar(self):
        print('Acelerando')
    
    def frear(self):
        print('Freando')

class Automovel:
    def __init__(self, aro, marca, volume_porta_mala): # Parâmetros da classe

        self.aro = aro # 1° Argumento
        self.marca = marca # 2° Argumento
        self.volume_porta_mala = volume_porta_mala # 3° Argumento
    
    def acelerar(self):
        print('Acelerando')
    
    def frear(self):
        print('Freando')

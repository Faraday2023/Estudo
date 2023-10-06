from classePai import*

class Motocicleta(Veículos):
    def __init__(self, aro, marca, qtde_raios_roda): # Parâmetros da classe

        Veículos.__init__(self,aro,marca)
        self.qtde_raios_roda = qtde_raios_roda # 3° Argumento
    
class Automóvel(Veículos):
    def __init__(self, aro, marca, volume_porta_mala): # Parâmetros da classe

        Veículos.__init__(self, aro, marca)
        self.volume_porta_mala = volume_porta_mala 
    
    def ligar_luz_teto(self):
        print('Luz ligada')
    
class Tablet:
    def __init__(self, armazenamento, ram, qtde_nucleos):
        self.armazenamento = armazenamento
        self.ram           = ram
        self.qtde_nucleos  = qtde_nucleos
    
    def instalar_app(self):
        print('Instalando app')

    def navegar_web(self):
        print('Navegando na web')
        
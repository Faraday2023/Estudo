cores = {

    'padrão': '\033[m',
    'azul': '\033[34m',
    'vermelho': '\033[31m', 
    'verde': '\033[32m', 
    'azul' : '\033[34m ',  
    'ciano' : '\033[36m', 
    'magenta' : '\033[35m', 
    'amarelo' : '\033[33m', 
    'preto' : ' \033[30m',  
    'branco' : '\033[37m',  
    'negro' : '\033[1m ', 
    'reverso' : '\033[2m' 

}

def leiaDinheiro(msg):
    válido = False

    while not válido:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() == True or entrada == '':
            print(f'{cores["vermelho"]} Erro, dados inválidos.{cores["padrão"]}')
        else:
            válido = True
        
    return float(entrada)


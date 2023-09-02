# Criando um sistema com cores

""" '\033[0:33:44m'  - Padrão para formatação de cores 

1) O primeiro dígito após o colchete indica o styles da letra;
2) O segundo a cor do texto;
3) O terceiro o plano de fundo.

Style                 Text           Back

0 - None              30             40
1 - Bold              31             41
4 - Underline         32             42
7 - Negative          33             43
                      34             44
                      35             45
                      36             46
                      37             47

OBS.: Para fechar um comando de cor no final precisa colocar '\033[m'

Exemplo:

print('\033[0:33:44m'Olá Mundo\033[m')
                                         
"""

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

print('Frase: {}{}{}'.format(cores['magenta'], 'Olá, mundo.',cores['padrão']))
"""Crie um código em python que teste se o site está acessível pelo computador usado"""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://academico.ifes.edu.br/qacademico/index.asp?t=2071')

except urllib.error.URLError:
    print('-'*50)
    print('O acadêmico não está disponível no momento')
    print('-'*50)

else:
    print('-'*50)
    print('Está tudo certo com o site')
    print('-'*50)

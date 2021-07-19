# Crie um programa que jogue Jokenpo com você:

import random
from time import sleep


print('\033[33m','=-='*5,{'JOKENPO!!!'},'=-='*5,'\033[m')
sleep(2)
escolhas = ['pedra','papel','tesoura']
print('Eu vou escolher primeiro, tá bom?')
sleep(2)
print('Escolhi. Agora é sua vez.')

jogada = str(input('\033[32mEscolha pedra, papel ou tesura: \033[m'))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

option = jogada.lower()
computador = random.choice(escolhas)
sleep(5)

if option == computador:
    print('\nEMPATOU!!!')
elif option == 'pedra' and computador == 'papel':
    print('\033[31m\n','Você perdeu!!\nEscolhi {} e {} perde para {}'.format(computador.upper(),option.upper(),computador.upper()),'\033[m')
elif option == 'pedra' and computador == 'tesoura':
    print('\033[32m\n','Você ganhou!!\nEscolhi {} e {} perde para {}'.format(computador.upper(),computador.upper(),option.upper()),'\033[m')
elif option == 'tesoura' and computador == 'pedra':
    print('\033[31m\n','Você perdeu!!\nEscolhi {} e {} perde para {}'.format(computador.upper(),option.upper(),computador.upper()),'\033[m')
elif option == 'tesoura' and computador == 'papel':
    print('\033[32m\n','Você ganhou!!\nEscolhi {} e {} perde para {}'.format(computador.upper(),computador.upper(),option.upper()),'\033[m')
elif option == 'papel' and computador == 'tesoura':
    print('\033[31m\n','Você perdeu!!\nEscolhi {} e {} perde para {}'.format(computador.upper(),option.upper(),computador.upper()),'\033[m')
elif option == 'papel' and computador == 'pedra':
    print('\033[32m\n','Você ganhou!!\nEscolhi {} e {} perde para {}'.format(computador.upper(),computador.upper(),option.upper()),'\033[m')

sleep(1)
print('')
print('\033[33m','=-='*5,'Foi bom jogar com você','=-='*5,'\nAté mais!!!!','\033[m')

## Refazer exercicio com condições aninhadas...
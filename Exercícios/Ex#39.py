# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # Se ele ainda vai se alistar.
    # Se é a hora de ele se alistar.
    # Se já passou do tempo para o alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou para ele se alistar.

from time import sleep
from datetime import date

print('\033[32m','-=-'*8,'\nCHAMADA DE ALISTAMENTO\n','-=-'*8,'\033[m')
sleep(3)
print('''\033[35m
Conforme as regras vigentes de alistamento todos os homens, ao completar 
18 (dezoito) anos necessitam se apresentar ao serviço militar brasileiro.
      
Caso você queira acompanhar quanto tempo falta para seu alistamento siga os passos abaixo:
      \033[m
      ''')
sleep(3)
nasc = int(input('Informe o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
sleep(5)
print('\n')

print('Então você tem {} anos em {}.\n'.format(idade, atual))

if idade == 18:
    print('\033[35mBem, parece que você completou a idade e precisa se alistar.\033[m')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('\033[32mAinda faltam {} ano(s) para que precise se apresentar ao serviço.'.format(saldo))
    print('Você deverá se alistar em {}.'.format(ano),'\033[m')
else:
    saldo = idade - 18
    ano = atual - saldo
    print('\033[31mVocê precisa se apresentar o mais rápido possível para o serviço.\nJá passaram {} ano(s) do seu prazo de alistamento'.format(idade - 18))
    print('Você deveria ter se alistado em {}.'.format(ano),'\033[m')
    
    
print('\nÉ isso por enquanto, foi bom ter ajudado.')
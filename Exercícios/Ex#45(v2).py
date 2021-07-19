# Crie um programa que jogue Jokenpo com você:
    # Usando condições aninhadas...
    # Com umm menú de Opções.

from random import randint
from time import sleep

# Dicionário de cores
cores = {
    'azul' : '\033[34m',
    'verde' : '\033[32m',
    'amarelo' : '\033[33m',
    'negativo' : '\033[7;30m',
    'magenta' : '\033[35m',
    'vermelho' : '\033[1;31m',
    'limpa' : '\033[m'
}

computador = randint(1, 3)
escolha = int(input('''
Escolha qual a sua opção:
[1] = Pedra
[2] = Papel
[3] = Tesoura
'''))

print('Escolhi ',computador)

if computador == 1:
    if escolha == 1:
        print('Empatou!!!')
    elif escolha == 2:
        print('Perdi, Pedra perde para papel.')
    elif escolha == 3:
        print('Ganhei, Pedra quebra Tesoura')
elif computador == 2:
    if escolha == 1:
        print('Ganhei, Pedra perde pra Papel')
    elif escolha == 2:
        print('Empatou!!!')
    elif escolha == 3:
        print('Perdi, Tesoura corta Papel.')
elif computador == 3:
    if escolha == 1:
        print('Perdi, Pedra quebra Tesoura.')
    elif escolha == 2:
        print('Ganhei, tesoura corta Papel')
    elif escolha == 3:
        print('Empatou')
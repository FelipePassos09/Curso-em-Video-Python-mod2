'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias do jogador.
'''

from random import randint,choice

computer = randint(0, 10)
com_pi = choice(['P','I'])
player = int(input('Escolha um número ente 0 e 10:\n'))
esc = str(input('Escolha se par ou impar [ P/I ]: \n')).strip().upper()
cont = 0

if (computer + player)%2 == 0:
    x = 'P'
if (computer + player)%2 != 0:
    x = 'I'

while True:
    cont += 1
    if esc not in ('P','I'):
        esc = str(input('Escolha se par ou impar [ P/I ]: \n')).strip().upper()
    while x == esc:
        cont += 1
        if x == 'P':
            result = 'PAR'
        if x == 'I':
            result = 'IMPAR'
        print(f'Parabéns, vocẽ ganhou\nEscolhi {computer} e {computer + player} é {result}, vamos continuar.')
        player = int(input('Escolha um número ente 0 e 10:\n'))
        esc = str(input('Escolha se par ou impar [ P/I ]: \n')).strip().upper()
        computer = randint(0, 10)
        com_pi = choice(['P','I'])
    if x != esc:
        break
        
if x == 'P':
    result = 'PAR'
if x == 'I':
    result = 'IMPAR'
    
print(f'Você perdeu em {cont} jogadas.\nEu escolhi {computer} e você {player} e {computer + player} é {result}.')
